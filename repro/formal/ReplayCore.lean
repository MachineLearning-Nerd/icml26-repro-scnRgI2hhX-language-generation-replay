import Init.Data.Int.Order
import Init.Data.List.Basic
import Lean.Elab.Tactic.Omega

/-!
Checked, dependency-free cores of the replay constructions in
"Language Generation with Replay".  This file deliberately proves quantified
statements rather than evaluating a finite window.
-/

namespace ReplayCore

def AllSupported (support : α → Prop) (xs : List α) : Prop :=
  ∀ x, x ∈ xs → support x

inductive ReplayTrace (support : α → Prop) (gen : List α → α) : List α → Prop
  | nil : ReplayTrace support gen []
  | target {xs x} : ReplayTrace support gen xs → support x →
      ReplayTrace support gen (xs ++ [x])
  | replay {xs prior} : ReplayTrace support gen xs →
      (∀ x, x ∈ prior → x ∈ xs) →
      ReplayTrace support gen (xs ++ [gen prior])

theorem replay_support_closure {α : Type u}
    (support : α → Prop) (gen : List α → α)
    (safe : ∀ prior, AllSupported support prior → support (gen prior))
    {xs : List α} (trace : ReplayTrace support gen xs) :
    AllSupported support xs := by
  induction trace with
  | nil =>
      intro x hx
      simp at hx
  | target trace hx ih =>
      intro y hy
      simp only [List.mem_append, List.mem_singleton] at hy
      cases hy with
      | inl h => exact ih y h
      | inr h => simpa [h] using hx
  | replay trace hprefix ih =>
      intro y hy
      simp only [List.mem_append, List.mem_singleton] at hy
      cases hy with
      | inl h => exact ih y h
      | inr h =>
          subst y
          apply safe
          intro z hz
          exact ih z (hprefix z hz)

def convertedGenerator
    (gen : List α → α) (burn : α) (threshold : Nat)
    (distinctCount : List α → Nat) (xs : List α) : α :=
  if threshold ≤ distinctCount xs then gen xs else burn

theorem converted_generator_safe {α : Type u}
    (support : α → Prop) (gen : List α → α) (burn : α)
    (threshold : Nat) (distinctCount : List α → Nat)
    (burnSupported : support burn)
    (standardSafe : ∀ xs, AllSupported support xs →
      threshold ≤ distinctCount xs → support (gen xs)) :
    ∀ xs, AllSupported support xs →
      support (convertedGenerator gen burn threshold distinctCount xs) := by
  intro xs hxs
  by_cases reached : threshold ≤ distinctCount xs
  · simp [convertedGenerator, reached, standardSafe xs hxs reached]
  · simp [convertedGenerator, reached, burnSupported]

theorem converted_generator_same_threshold {α : Type u}
    (support : α → Prop) (gen : List α → α) (burn : α)
    (threshold : Nat) (distinctCount : List α → Nat)
    (standardGuarantee : ∀ xs, AllSupported support xs →
      threshold ≤ distinctCount xs → support (gen xs) ∧ gen xs ∉ xs)
    (xs : List α) (hxs : AllSupported support xs)
    (reached : threshold ≤ distinctCount xs) :
    support (convertedGenerator gen burn threshold distinctCount xs) ∧
      convertedGenerator gen burn threshold distinctCount xs ∉ xs := by
  simpa [convertedGenerator, reached] using standardGuarantee xs hxs reached

def Consistent (support : Nat → Nat → Prop) (sure : Nat → Prop)
    (candidate : Nat) : Prop :=
  ∀ x, sure x → support candidate x

def Critical (support : Nat → Nat → Prop) (sure priorOutputs : Nat → Prop)
    (candidate prefixBound : Nat) : Prop :=
  Consistent support sure candidate ∧
    ∀ earlier, earlier < candidate → Consistent support sure earlier →
      ∀ x, x ≤ prefixBound → support candidate x → ¬ priorOutputs x →
        support earlier x

theorem criticality_monotone_in_prefix
    (support : Nat → Nat → Prop) (sure priorOutputs : Nat → Prop)
    (candidate small large : Nat) (hbound : small ≤ large)
    (critical : Critical support sure priorOutputs candidate large) :
    Critical support sure priorOutputs candidate small := by
  constructor
  · exact critical.1
  · intro earlier hearlier hconsistent x hx hsupported hnew
    exact critical.2 earlier hearlier hconsistent x (Nat.le_trans hx hbound)
      hsupported hnew

theorem sure_observation_is_target
    (target priorOutputs : α → Prop) (x : α)
    (admissible : target x ∨ priorOutputs x) (notReplay : ¬ priorOutputs x) :
    target x := by
  rcases admissible with htarget | hreplay
  · exact htarget
  · exact False.elim (notReplay hreplay)

theorem finite_exclusion_cannot_block_uus
    (support : α → Prop)
    (outsideEveryFinite : ∀ forbidden : List α,
      ∃ x, support x ∧ x ∉ forbidden)
    (forbidden : List α) :
    ∃ output, support output ∧ output ∉ forbidden :=
  outsideEveryFinite forbidden

def InfinitelyOften (event : Nat → Prop) : Prop :=
  ∀ after, ∃ time, after ≤ time ∧ event time

def EventuallyNever (event : Nat → Prop) : Prop :=
  ∃ after, ∀ time, after ≤ time → ¬ event time

theorem infinite_or_eventually_never (event : Nat → Prop) :
    InfinitelyOften event ∨ EventuallyNever event := by
  classical
  by_cases often : InfinitelyOften event
  · exact Or.inl often
  · right
    apply Classical.byContradiction
    intro notEventually
    apply often
    intro after
    apply Classical.byContradiction
    intro noLaterEvent
    apply notEventually
    refine ⟨after, ?_⟩
    intro time htime hevent
    apply noLaterEvent
    exact ⟨time, htime, hevent⟩

theorem proper_diagonalization_dichotomy
    (nonReference error : Nat → Prop)
    (diagonalError : ∀ time, nonReference time → error time)
    (finalTrapError : EventuallyNever nonReference →
      ∃ after, ∀ time, after ≤ time → error time) :
    InfinitelyOften error := by
  rcases infinite_or_eventually_never nonReference with often | eventually
  · intro after
    rcases often after with ⟨time, htime, hnonref⟩
    exact ⟨time, htime, diagonalError time hnonref⟩
  · rcases finalTrapError eventually with ⟨start, herror⟩
    intro after
    let time := max after start
    refine ⟨time, Nat.le_max_left _ _, ?_⟩
    exact herror time (Nat.le_max_right _ _)

theorem withheld_phase_outputs_force_infinite_errors
    (stage : Nat → Nat) (invalid : Nat → Prop)
    (stageAfterPhase : ∀ phase, phase ≤ stage phase)
    (invalidAtStage : ∀ phase, invalid (stage phase)) :
    InfinitelyOften invalid := by
  intro after
  exact ⟨stage after, stageAfterPhase after, invalidAtStage after⟩

def hInf (x : Int) : Prop := 1 ≤ x

def hFinite (d x : Int) : Prop :=
  (1 ≤ x ∧ x ≤ d) ∨ x < 0

theorem countable_intersection_exact (d x : Int) :
    hInf x ∧ hFinite d x ↔ 1 ≤ x ∧ x ≤ d := by
  simp only [hInf, hFinite]
  constructor
  · rintro ⟨hx, hfd⟩
    rcases hfd with hfd | hneg
    · exact hfd
    · omega
  · rintro h
    exact ⟨h.1, Or.inl h⟩

theorem countable_intersection_exhausted (d x : Int)
    (joint : hInf x ∧ hFinite d x) : ¬ (d < x) := by
  have hx := (countable_intersection_exact d x).mp joint
  omega

def h1Minus (x : Int) : Prop := x ≤ 0 ∨ x = 1
def h2Minus (x : Int) : Prop := x ≤ 0 ∨ x = 2
def h1Plus (x : Int) : Prop := 0 ≤ x ∨ x = -1
def h2Plus (x : Int) : Prop := 0 ≤ x ∨ x = -2

theorem plus_intersection_exact (x : Int) :
    h1Plus x ∧ h2Plus x ↔ 0 ≤ x := by
  simp only [h1Plus, h2Plus]
  constructor
  · rintro ⟨h1, h2⟩
    rcases h1 with h1 | h1 <;> rcases h2 with h2 | h2
    · exact h1
    · exact h1
    · exact h2
    · omega
  · intro hx
    exact ⟨Or.inl hx, Or.inl hx⟩

theorem minus_intersection_exact (x : Int) :
    h1Minus x ∧ h2Minus x ↔ x ≤ 0 := by
  simp only [h1Minus, h2Minus]
  constructor
  · rintro ⟨h1, h2⟩
    rcases h1 with h1 | h1 <;> rcases h2 with h2 | h2
    · exact h1
    · exact h1
    · exact h2
    · omega
  · intro hx
    exact ⟨Or.inl hx, Or.inl hx⟩

theorem minus_replays_legal :
    h1Minus (-1) ∧ h1Minus (-2) ∧ h2Minus (-1) ∧ h2Minus (-2) := by
  simp [h1Minus, h2Minus]

theorem plus_replays_legal :
    h1Plus 1 ∧ h1Plus 2 ∧ h2Plus 1 ∧ h2Plus 2 := by
  simp [h1Plus, h2Plus]

theorem h1Minus_not_subset_plus_intersection :
    ¬ (∀ x, h1Minus x → h1Plus x ∧ h2Plus x) := by
  intro h
  have hmember : h1Minus (-2) := by simp [h1Minus]
  have hbound : 0 ≤ (-2 : Int) := (plus_intersection_exact (-2)).mp (h (-2) hmember)
  omega

theorem h2Minus_not_subset_plus_intersection :
    ¬ (∀ x, h2Minus x → h1Plus x ∧ h2Plus x) := by
  intro h
  have hmember : h2Minus (-1) := by simp [h2Minus]
  have hbound : 0 ≤ (-1 : Int) := (plus_intersection_exact (-1)).mp (h (-1) hmember)
  omega

theorem h1Plus_not_subset_plus_intersection :
    ¬ (∀ x, h1Plus x → h1Plus x ∧ h2Plus x) := by
  intro h
  have hmember : h1Plus (-1) := by simp [h1Plus]
  have hbound : 0 ≤ (-1 : Int) := (plus_intersection_exact (-1)).mp (h (-1) hmember)
  omega

theorem h2Plus_not_subset_plus_intersection :
    ¬ (∀ x, h2Plus x → h1Plus x ∧ h2Plus x) := by
  intro h
  have hmember : h2Plus (-2) := by simp [h2Plus]
  have hbound : 0 ≤ (-2 : Int) := (plus_intersection_exact (-2)).mp (h (-2) hmember)
  omega

theorem h1Minus_not_subset_minus_intersection :
    ¬ (∀ x, h1Minus x → h1Minus x ∧ h2Minus x) := by
  intro h
  have hmember : h1Minus 1 := by simp [h1Minus]
  have hbound : (1 : Int) ≤ 0 := (minus_intersection_exact 1).mp (h 1 hmember)
  omega

theorem h2Minus_not_subset_minus_intersection :
    ¬ (∀ x, h2Minus x → h1Minus x ∧ h2Minus x) := by
  intro h
  have hmember : h2Minus 2 := by simp [h2Minus]
  have hbound : (2 : Int) ≤ 0 := (minus_intersection_exact 2).mp (h 2 hmember)
  omega

theorem h1Plus_not_subset_minus_intersection :
    ¬ (∀ x, h1Plus x → h1Minus x ∧ h2Minus x) := by
  intro h
  have hmember : h1Plus 1 := by simp [h1Plus]
  have hbound : (1 : Int) ≤ 0 := (minus_intersection_exact 1).mp (h 1 hmember)
  omega

theorem h2Plus_not_subset_minus_intersection :
    ¬ (∀ x, h2Plus x → h1Minus x ∧ h2Minus x) := by
  intro h
  have hmember : h2Plus 1 := by simp [h2Plus]
  have hbound : (1 : Int) ≤ 0 := (minus_intersection_exact 1).mp (h 1 hmember)
  omega

theorem common_plus_halfline_is_subset (x : Int) :
    0 ≤ x → h1Plus x ∧ h2Plus x := by
  intro hx
  exact (plus_intersection_exact x).mpr hx

theorem common_minus_halfline_is_subset (x : Int) :
    x ≤ 0 → h1Minus x ∧ h2Minus x := by
  intro hx
  exact (minus_intersection_exact x).mpr hx

inductive ProperHypothesis
  | h1Minus | h2Minus | h1Plus | h2Plus
  deriving DecidableEq

def properSupport : ProperHypothesis → Int → Prop
  | .h1Minus => h1Minus
  | .h2Minus => h2Minus
  | .h1Plus => h1Plus
  | .h2Plus => h2Plus

def ambiguousTargets : ProperHypothesis → ProperHypothesis × ProperHypothesis
  | .h1Minus => (.h1Plus, .h2Plus)
  | .h2Minus => (.h1Plus, .h2Plus)
  | .h1Plus => (.h1Minus, .h2Minus)
  | .h2Plus => (.h1Minus, .h2Minus)

theorem every_first_output_has_ambiguous_targets (first : ProperHypothesis) :
    let targets := ambiguousTargets first
    (∃ replayA replayB,
      properSupport first replayA ∧ properSupport first replayB ∧
      properSupport targets.1 replayA ∧ properSupport targets.2 replayB) ∧
    ∀ output, ¬ (∀ x, properSupport output x →
      properSupport targets.1 x ∧ properSupport targets.2 x) := by
  cases first <;> constructor
  · exact ⟨-1, -2, by simp [properSupport, h1Minus], by simp [properSupport, h1Minus],
      by simp [ambiguousTargets, properSupport, h1Plus],
      by simp [ambiguousTargets, properSupport, h2Plus]⟩
  · intro output
    cases output
    · simpa [ambiguousTargets, properSupport] using h1Minus_not_subset_plus_intersection
    · simpa [ambiguousTargets, properSupport] using h2Minus_not_subset_plus_intersection
    · simpa [ambiguousTargets, properSupport] using h1Plus_not_subset_plus_intersection
    · simpa [ambiguousTargets, properSupport] using h2Plus_not_subset_plus_intersection
  · exact ⟨-1, -2, by simp [properSupport, h2Minus], by simp [properSupport, h2Minus],
      by simp [ambiguousTargets, properSupport, h1Plus],
      by simp [ambiguousTargets, properSupport, h2Plus]⟩
  · intro output
    cases output
    · simpa [ambiguousTargets, properSupport] using h1Minus_not_subset_plus_intersection
    · simpa [ambiguousTargets, properSupport] using h2Minus_not_subset_plus_intersection
    · simpa [ambiguousTargets, properSupport] using h1Plus_not_subset_plus_intersection
    · simpa [ambiguousTargets, properSupport] using h2Plus_not_subset_plus_intersection
  · exact ⟨1, 2, by simp [properSupport, h1Plus], by simp [properSupport, h1Plus],
      by simp [ambiguousTargets, properSupport, h1Minus],
      by simp [ambiguousTargets, properSupport, h2Minus]⟩
  · intro output
    cases output
    · simpa [ambiguousTargets, properSupport] using h1Minus_not_subset_minus_intersection
    · simpa [ambiguousTargets, properSupport] using h2Minus_not_subset_minus_intersection
    · simpa [ambiguousTargets, properSupport] using h1Plus_not_subset_minus_intersection
    · simpa [ambiguousTargets, properSupport] using h2Plus_not_subset_minus_intersection
  · exact ⟨1, 2, by simp [properSupport, h2Plus], by simp [properSupport, h2Plus],
      by simp [ambiguousTargets, properSupport, h1Minus],
      by simp [ambiguousTargets, properSupport, h2Minus]⟩
  · intro output
    cases output
    · simpa [ambiguousTargets, properSupport] using h1Minus_not_subset_minus_intersection
    · simpa [ambiguousTargets, properSupport] using h2Minus_not_subset_minus_intersection
    · simpa [ambiguousTargets, properSupport] using h1Plus_not_subset_minus_intersection
    · simpa [ambiguousTargets, properSupport] using h2Plus_not_subset_minus_intersection

theorem cantor_diagonal_not_enumerable (enumerated : Nat → Nat → Prop) :
    ∃ diagonal : Nat → Prop, ∀ n, ¬ (∀ x, diagonal x ↔ enumerated n x) := by
  let diagonal : Nat → Prop := fun n => ¬ enumerated n n
  refine ⟨diagonal, ?_⟩
  intro n equal
  have atDiagonal := equal n
  simp [diagonal] at atDiagonal

end ReplayCore
