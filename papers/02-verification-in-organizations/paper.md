# Verification as a Public Good: Groups, Protection Delegation and Action-Bound Rules against Social Engineering

> **DRAFT.** Work in progress, not peer reviewed and not empirically validated. Derived from the working paper *Trust is Engineered* v0.7 ([long version](../../docs/trust-is-engineered.md)); identifiers and evidence status follow it.

Johannes Rumpf ([ORCID 0009-0001-8675-0608](https://orcid.org/0009-0001-8675-0608)) · Version 0.2 · 22 October 2026 · DOI [10.5281/zenodo.23813118](https://doi.org/10.5281/zenodo.23813118)

## Abstract

Social engineering exploits trust, yet training people to detect deception achieves little. This paper applies a graph-based evidence model of trust to the level at which information security is actually practiced: the team, the department and the organization. Its central claim is that groups act less on the evaluation of evidence than on verification. Through diffusion of responsibility, protection delegation (“That's IT's job”) and descriptive norms, verification becomes a public good that is undersupplied. Two derived quantities make this explicit: the verification coverage C of a group and the effective trust E′ after presumed filtering by a security institution. Both are instances of one term in the model's verification rule, the coverage an actor attributes to other nodes; from that rule the paper derives that coverage falls with the number of unassigned verifiers and rises with the loss at stake, and it states which predictions this adds beyond the bystander, risk-compensation and free-riding literatures that describe the same structure. The threshold rule of the model suggests that verification should be triggered by the action class, not by trust in the sender. The paper further argues that trust dimensions and security objectives lie on two axes, actor and asset, and therefore form a matrix rather than a mapping; authenticity acts as an anchor beneath all rows. It derives twenty-four security rules ranked by size of the loss, states the hypotheses with their evidence status and lists testable predictions. All derivations are model statements. They have not been empirically tested, and the rules have not been evaluated as a package.

**Keywords:** social engineering; verification; diffusion of responsibility; protection delegation; descriptive norms; security objectives; trust model

Identifiers G (core assumption), H (hypothesis), V (prediction) and S (rule) follow the long version [Rumpf 2026a, v0.7] so that they stay stable across papers.

## 1. Introduction

AI-generated content, deepfakes and synthetic identities change the conditions under which people trust requests. Content alone no longer determines credibility; what matters is where a request comes from and through which channel it arrives.

This paper addresses one practical problem (long version, Section 1.3). **Problem A:** How do people learn to recognize abuse of trust such as phishing and social engineering with little effort and a high hit rate, without rejecting legitimate requests across the board? An entity must decide which action it allows another entity under incomplete evidence.

Between the macro level (public sphere, institutions) and the micro level (individual trust decisions) lies the meso level of teams, departments and organizations, in which security decisions are actually made. This paper deals with the meso level and with the rules that follow from it.

The contribution has four parts:

1. **Groups act on verification, not on evaluation,** through diffusion of responsibility, protection delegation and descriptive norms (Section 4). Diffusion of responsibility and protection delegation share one structure, perceived coverage by others, and their dependence on group size and loss is derived from the verification rule (Section 4.8).
2. **Verification is triggered by the action class,** not by trust in the sender (Section 6).
3. **Trust dimensions and security objectives form a matrix,** not a mapping (Section 7).
4. **Security rules ranked by loss** (Section 8).

The core model is developed in Paper 1 (Rumpf 2026b); human-agent and machine-machine trust are treated in Paper 3 (Rumpf 2026c).

## 2. Related work

The paper builds on the definition of trust as willingness to be vulnerable (Mayer et al. 1995; Rousseau et al. 1998) and on Subjective Logic (Jøsang 2016). For the meso level it draws on conformity (Asch 1951; Bond & Smith 1996), information cascades (Bikhchandani et al. 1992), diffusion of responsibility (Darley & Latané 1968; Latané & Darley 1970; Fischer et al. 2011), the volunteer's dilemma (Diekmann 1985) and descriptive norms (Cialdini et al. 1990), and on measurements of these mechanisms in security and fraud settings (Zhang, Reithel & Li 2009; Brink, Eller & Gan 2015; Paravastu, Simmers & Anandarajan 2018). From usable security it takes the rational rejection of security advice (Herley 2009), the compliance budget (Beautement et al. 2008) and field evidence on phishing training (Ho et al. 2025), and for security objectives ISO/IEC 27000:2018, FIPS 199 and Parker (1998). A detailed comparison with prior work is given in the accompanying document [related-work.md](related-work.md).

## 3. The model in brief

This section summarizes only the quantities used here. The full model is given in Paper 1 (Rumpf 2026b) and in the long version (Chapters 3 to 6).

**Opinion.** Trust is modeled as a directed graph of entities. Each edge carries, per context c and dimension k, an opinion instead of a scalar:

```math
\omega_{A\to B,c,k} = (b,\; d,\; u,\; a), \qquad b + d + u = 1
```

b is trust, d distrust, u uncertainty, a the base rate (prior). The representation follows Subjective Logic (Jøsang 2016). Each edge keeps two evidence accounts, r for positive and s for negative evidence, together with the base rate a and the prior strength W:

```math
b = \frac{r}{r+s+W}, \qquad d = \frac{s}{r+s+W}, \qquad u = \frac{W}{r+s+W}, \qquad E = b + a\,u
```

E is the expected trustworthiness (Beta Reputation System; Jøsang & Ismail 2002). Separating b, d and u distinguishes ignorance from ambivalence, and the epistemic bubble from the echo chamber (Section 4.7).

**Source dependence.** Repeated statements from dependent sources count only as an effective sample. For n repetitions with dependence D:

```math
n_{\text{eff}} = \frac{n}{1 + (n-1)\,D}, \qquad \lim_{n\to\infty} n_{\text{eff}} = \frac{1}{D}
```

At D = 1 (one original source), n_eff = 1, no matter how often the statement appears.

**Normative and descriptive account.** The normative account weights evidence by independence and diagnosticity q (how costly a signal would be for a deceiver); the descriptive account adds familiarity from repetition. Their difference is the calibration gap:

```math
\Gamma_{A\to B,c} = E^{\text{desc}} - E^{\text{norm}}
```

Γ > 0 means unjustified trust (False Trust), Γ < 0 unjustified distrust (False Distrust). **Γ is the attack surface for social engineering and at the same time the target quantity for training.** Decisions are made only on the basis of the normative account.

**Three questions.** A trust decision breaks down into three checks that do not substitute for one another (long version, Section 6.1): identity (who is the entity?), authorization (may it trigger this action? permission P) and factual correctness (is the specific request correct?). **A confirmed identity proves neither permission nor correctness.** Trust in the person proves none of the three.

**Threshold rule.** An action x yields the benefit N for a legitimate request and the loss L in case of abuse. It is only worthwhile if the probability of legitimacy exceeds the threshold θ:

```math
\theta_x = \frac{L_x}{L_x + N_x}
```

The permission is granted if the normative trust minus an uncertainty penalty reaches the threshold:

```math
E^{\text{norm}} - \kappa\,u \;\ge\; \theta_x
```

κ is the risk aversion. **The threshold depends only on the action, not on the person.** Example: a bank transfer with L = EUR 50,000 and N = EUR 500 yields θ ≈ 0.99. No realistically attainable personal trust suffices on its own.

**Verification rule.** An additional verification with cost K and detection probability τ is worthwhile if:

```math
K \;<\; \tau \cdot (1 - E^{\text{norm}}) \cdot L_x
```

**Verifications must therefore be cheap so that they are still triggered when residual doubt is small.** In organizations, K and τ are not set individually but by norm, role and the presumed verification by others (Section 4).

**Base-rate shifts.** A news item or event about a category shifts the base rate a of that category. The effect on an individual edge is:

```math
\Delta E = u \cdot \Delta a
```

Edges with little evidence are hit fully, well-evidenced edges hardly at all.

## 4. Groups and organization

Information security is lived in teams. There it also matters which evidence reaches A at all, how the group interprets it, and whether A verifies personally or tacitly leaves it to others. **Groups act at all three stages, and they act above all on verification, not on evaluation.** This explains why individual awareness training achieves so little (Section 6.1): it addresses the individual's evaluation, while verification behavior is determined by role, norm and perceived coverage by others.

This section is a derivation from the model and from social-psychological literature mostly not collected in security contexts (long version, Chapter 7).

Between the macro and the micro level lies the level at which security decisions are actually made:

| Level | Unit | Typical action | Where treated |
| --- | --- | --- | --- |
| Micro | edge A→B | payment, approval, data disclosure | Paper 1 (Rumpf 2026b); Section 6 |
| Meso | team, department, organization | verifying, reporting, following or circumventing norms | this section |
| Macro | public, categories | assent, sharing, turning away | long version, Section 12.4; [Case Study 1](../../docs/case-study-01-populist-techniques.md) |

### 4.1 Three stages at which groups act

| Stage | Question | Model variables | Key finding |
| --- | --- | --- | --- |
| Evidence intake | Which evidence reaches A? | D, R, n_eff | Groups share sources; D within the group is high |
| Interpretation | How does A evaluate it? | B, a, W, v, w± | Group beliefs color valence and dimension |
| Verification | Does A verify, or someone else? | K, τ, verification coverage C | In groups, verification is a public good and is undersupplied |

R is perceived repetition, B beliefs, v valence, w± dimension weights (long version, Section 6.4). The third stage is new and the most important one for information security.

Three findings are considered established and form core assumption G4 (Section 9.1). Visible judgments of others shift one's own judgments, even when the evidence is unambiguous (Asch 1951; Bond & Smith 1996). Decisions of others are adopted as evidence, even if they in turn are based only on imitation (information cascade; Bikhchandani, Hirshleifer & Welch 1992). And the willingness to act decreases with the number of possible actors (Darley & Latané 1968; Fischer et al. 2011).

### 4.2 Verification as a public good

If an action can be verified by n persons and each decides independently and verifies with probability c_n, the verification coverage is:

```math
C = 1 - (1 - c_n)^n
```

In general, C is the probability that at least one person verifies, 1 − P(nobody verifies); the formula is the special case of independent decisions. With dependent decisions, C can be lower or higher than the formula gives; if all decide together, C = c_n.

Empirically, c_n decreases with n faster than the larger exponent compensates. Each individual applies the verification rule not to (1−E), but to the residual risk after the presumed verification by the others. If everyone presumes the same, nobody verifies; Section 4.8 derives the decrease from the verification rule. **Two possible verifiers without assigned responsibility often amount to less than one verification.**

The four-eyes principle therefore protects only if both verifiers are explicitly responsible and verify independently. If both see the same justification via the same channel, their dependence D is close to 1, and the second verification has almost no evidential value. The same holds for correlated verifiers among agents (long version, Section 10.7; Paper 3 (Rumpf 2026c)).

### 4.3 Protection delegation: “That's IT's job”

A holds an edge to the security institution I (IT, security, compliance) in the context “defense against attacks”. This edge has three properties:

1. **High base rate a**, institutionally grounded (relationship type institutional).
2. **u close to 1**, because successful defense is invisible. A sees only what gets through and assumes it has been checked. This is a survivorship bias on the evidence side.
3. **No feedback on errors**, as long as nothing happens.

In the verification rule, A does not calculate with E_norm(B), but with the value after presumed filtering:

```math
E' = 1 - (1 - E)\,(1 - \tau_I)
```

τ_I is the detection rate of the institution as assumed by A. With τ_I close to 1, (1−E′) tends to 0, and **no verification of one's own is worthwhile any longer, for any loss L.** In fact, τ_I is below 1. Filters let part of the attacks through, and precisely this part reaches A.

The calibration gap here lies not on A→B but on A→I: Γ_{A→I} > 0. **It acts as a multiplier on all edges A→B within the institution's area of responsibility.** In the model, “It's IT's job to protect us” is not an attitude problem but a rationally applied verification rule with a miscalibrated τ_I. A related phenomenon is risk compensation: perceived protection increases risk behavior (Peltzman 1975; Wilde 1982); in a security survey, perceived technical protection lowered the intention to comply with security policy (Zhang, Reithel & Li 2009). As for platforms, a guarantee by IT is itself only a source of evidence with its own uncertainty; for employees, IT is the platform.

Because u is high on A→I, ΔE = u·Δa implies that a single visible incident hits the edge in full: “IT protects us” flips to “IT is useless”, without any calibrated assessment in between. Both states are miscalibrations; the second produces security fatigue and circumvention (Stanton et al. 2016). The remedy is not more trust in the institution, but visible evidence about its error rate (rule S22).

### 4.4 Norms beat knowledge

Whether A verifies depends more on what A considers usual (descriptive norm) than on what A knows or what is prescribed (Cialdini, Reno & Kallgren 1990). In the model, the descriptive norm sets the verification cost K. A verification that counts as distrust in the team is socially expensive; one that counts as a matter of course is cheap. **K is a group variable, not an individual one.** This refines rule S14: cheap means above all socially cheap. Herley (2009) shows the flip side: where security rules cost the individual effort but bring the benefit to others, rejecting them is individually rational.

The matching attack is normalization (“Everyone here does it this way”). It lowers τ and raises K without changing a single evaluation: a calibration attack (Section 5) on the verification stage.

### 4.5 Groups as an attack surface

| Attack | Group effect | Model variable |
| --- | --- | --- |
| Compromised colleague account | in-group prior, little discounting within the group | G, H4 |
| CEO fraud | authority in the group plus diffusion of responsibility (“Accounting will check it”) | a, C |
| Supplier and project fraud | swift trust: high base rate with u close to 1 in temporary teams (Meyerson, Weick & Kramer 1996) | a, u, V9 |
| Normalization of rule violations | descriptive norm | K, τ |
| Internal consensus (“We all saw it”) | cascade, D close to 1 | n_eff |
| Blame after an incident | black sheep effect (Marques, Yzerbyt & Leyens 1988): deviants from one's own group are judged more harshly; reporting does not happen | s, S17 |

G is the group prior. V9 (long version) predicts that in one-off contacts category signals remain decisive because u stays close to 1. H4 and H4a (long version; Paper 1 (Rumpf 2026b)) state that referrals are discounted too little, least within the in-group.

### 4.6 Groups as a protective factor

The same mechanisms calibrate when the sources are independent (D low) and the signals cost something (q high). Whether a group effect helps depends on D and q, not on the effect itself.

| Effect | Model variable | Condition |
| --- | --- | --- |
| Assigned verification role | C, c_n | one named person per action class, no “someone” |
| Independent second verification | D of the verifiers | different channel, different information, own responsibility |
| Psychological safety (Edmondson 1999) | s is reported | errors without sanction (S17) |
| Structured dissent, red team (Janis 1972 as the negative example) | enforced s | group variant of Consider the Opposite |
| Wisdom of crowds | n_eff | only without mutual influence (Lorenz et al. 2011) |
| Gossip as a reputation system | propagation of trust information (long version, G2) | D low (Sommerfeld et al. 2007) |
| Contact across group boundaries (Allport 1954; Pettigrew & Tropp 2006) | group prior G replaced by individual evidence | breaks the learning trap |

The learning trap: below the interaction threshold, no corrective evidence arrives (long version, Section 5.4).

### 4.7 Echo chamber and bubble

Nguyen (2020) distinguishes the epistemic bubble, in which other sources are simply absent, from the echo chamber, in which outside sources are discredited in advance. In the model, the bubble is a u-state towards outside sources, the chamber a d-state. They call for opposite countermeasures: contact with outside sources dissolves the bubble and confirms the chamber. **A single trust value could not distinguish between the two.** This is at the same time the collective form of the learning trap: groupthink (Janis 1972) is a group below the interaction threshold towards everything that comes from outside.

### 4.8 Perceived coverage by others: one structure behind 4.2 and 4.3

Sections 4.2 and 4.3 describe two mechanisms, but one structure. In both, A applies the verification rule not to the residual risk (1 − E), but to the residual risk after the verification that A attributes to other nodes. Let τ̂_O be the detection rate that A attributes to all other nodes O that could also verify the action:

```math
K \;<\; \tau \cdot (1 - E)\,(1 - \hat{\tau}_O) \cdot L
```

Protection delegation (4.3) is the case O = {I} with τ̂_O = τ_I. Diffusion of responsibility (4.2) is the case in which O consists of the n − 1 colleagues, each presumed to verify with probability ĉ and, when verifying, to detect the attack with probability τ̂, so that τ̂_O = 1 − (1 − τ̂ĉ)^(n−1). The two combine multiplicatively: 1 − τ̂_O = (1 − τ_I)(1 − τ̂ĉ)^(n−1). **Trust is not the cause of either effect but its weight:** τ_I, τ̂ and ĉ are A's opinions about the competence and diligence of the institution and of the colleagues in the context “verification”.

**What the rule derives.** Let ρ = K / (τ (1 − E) L) be the ratio of verification cost to the expected loss prevented (ρ < 1, otherwise nobody verifies even alone). A potential verifier verifies as long as (1 − τ̂ĉ)^(n−1) > ρ. If every potential verifier presumes the same of the others and applies the same rule, and if a colleague's verification is presumed to detect the attack with certainty (τ̂ = 1), the symmetric solution at which nobody gains by deviating is:

```math
c_n = 1 - \rho^{\,1/(n-1)}, \qquad C = 1 - \rho^{\,n/(n-1)}
```

For n = 1, C = 1; for n = 2, C = 1 − ρ²; as n grows, C falls monotonically towards 1 − ρ. This is the volunteer's dilemma (Diekmann 1985) with verification as the volunteered act. With imperfect peer detection (τ̂ < 1), the interior solution satisfies τ̂·c_n = 1 − ρ^(1/(n−1)), so each colleague verifies more often by the factor 1/τ̂, and 1 − ρ^(n/(n−1)) is then the detection coverage 1 − (1 − τ̂c_n)^n rather than C; it exists only if ρ ≥ (1 − τ̂)^(n−1), and below that bound everyone verifies and C = 1. Two statements that Section 4.2 made only empirically follow: c_n falls with n fast enough that C falls too, and coverage rises with the loss L and falls with the verification cost K and the trust E in the sender. The second turns the main moderator of the bystander literature, a weaker effect in dangerous emergencies (Fischer et al. 2011), into a prediction: diffusion is strongest where the action looks harmless, which is where social engineering operates (V28). The solution assumes that A knows n, treats the others as alike, presumes their detection rate and applies the rule as a threshold; it is a model statement, not a finding.

![More possible verifiers, less coverage](../../docs/figures/fig-11-verification-coverage.png)

*Figure 1: Verification coverage C against the number of possible verifiers n · symmetric solution for three values of ρ with perceived peer detection τ̂ = 1; a named role keeps C = 1*

**What the model imports.** The rule does not explain why A presumes coverage by others at all; that is core assumption G4 and comes from the bystander literature, which names three processes (Latané & Darley 1970). The model keeps them apart because they act on different variables: diffusion of responsibility (“someone else will check”) is τ̂_O in the verification rule (H17); pluralistic ignorance (“nobody reacts, so it is harmless”) is inaction of others taken as evidence with D close to 1 (V23); audience inhibition (“if I am wrong, I look distrustful”) is the social part of K (Section 4.4, H18). Studies in security contexts usually measure these together, as an intention to report or to act (Brink, Eller & Gan 2015; Paravastu, Simmers & Anandarajan 2018); the separation is what makes H17, H18 and V23 testable one at a time.

**The same structure in other literatures.** Read as perceived coverage by other nodes, the effect is recognizable in fields that rarely cite one another: risk compensation and risk homeostasis (Peltzman 1975; Wilde 1982; in security, Zhang, Reithel & Li 2009), where technical protection is the covering node; automation complacency (Parasuraman & Manzey 2010); free riding in public goods, with security as a best-shot good (Varian 2004; Grossklags, Christin & Chuang 2008), of which C is the aggregate; the volunteer's dilemma (Diekmann 1985); social loafing, which supplies effect sizes per group size (Karau & Williams 1993); and the redundancy problem, in which each safeguard relies on the others (Sagan 2004), the closest precedent for the D argument of Section 4.2.

**What the abstraction buys, and where it ends.** The unification is worth keeping only where it yields a statement that the source literatures do not make. Four can be tested:

1. **Independent verifications, not verifiers.** Bystander studies count heads. Coverage C counts whether anyone verifies at all, but a verification by someone who sees the same request through the same channel adds almost no evidence, because the dependence D of the verifiers is close to 1 (Section 4.2, V24, S21). What protects is the number of independent verifications, not the number of verifiers.
2. **Multiplicative combination.** H16 and H17 multiply: a team with high trust in the security institution and several unnamed verifiers is the worst case (V29). Each source literature sees only one factor.
3. **Loss dependence.** c_n rises with L (V28); an empirical moderator in the bystander literature, derived here.
4. **Trust in the others as the weight.** High trust in the colleagues' competence raises τ̂_O and lowers one's own verification, while in-group membership lowers the social part of K. The two channels pull in opposite directions, and which one dominates is set by the context: by the loss L (shared and visible in a fire, borne by someone else in an assault, small and inconspicuous in a routine verification) and by what K contains (physical risk, social cost, or both). Bystander research finds that in-group bystanders can raise rather than lower intervention in violence scenarios (Levine & Crowther 2008); the K channel accounts for this, the τ̂_O channel does not. The model therefore does not predict the sign of the in-group effect in general, only that it follows L and K of the action class in question.

The tipping dynamics of V22 come from the evidence model and have no counterpart in these literatures either. Beyond these statements, “perceived coverage” becomes a label. The model does not derive the bystander effect from first principles; it subsumes it. What it derives is the dependence of c_n on n and on ρ; what it imports is that people presume coverage at all (G4). A reviewer can object that H17 is the bystander effect with Greek letters; the answer is the four statements above, not the relabeling. Section 9.3 therefore keeps “derived” and “transferred” apart.

## 5. Attacks on groups as operations on model quantities

**Two classes of attack.** Abuse attacks exploit a scope of action P that has already been granted; their loss follows G1. Calibration attacks instead shift the evaluation itself: they enlarge the calibration gap Γ without touching any permission. Social engineering usually combines both stages: first calibrate, then abuse (long version, Section 8.2).

Every social engineering technique can be read as an intervention in a specific model variable (long version, Section 8.4). For groups and organizations: an authority or group signal raises the base rate a without evidence (verify permission separately from status); time pressure and secrecy raise the verification cost K (make verification mandatory per action class); normalization acts on the descriptive norm and K (S23); exploiting protection delegation acts on τ_I (S22); a compromised colleague account exploits weak discounting within the in-group (S1).

The techniques occur in combination. Example: a fraudulent identity is visible on several platforms for months, collects seemingly independent recommendations and then makes a payment request under time pressure. R is high, D close to 1, q low, K artificially raised.

## 6. Application: verify the action, do not detect deception

**The goal is calibrated trust, neither maximum trust nor maximum distrust.** Training is meant to reduce the calibration gap Γ in both directions.

### 6.1 What the evidence says about training

- People detect lies with a hit rate of about 54 percent (Bond & DePaulo 2006); training improves this only slightly (Hauch et al. 2016).
- In a randomized trial with about 19,500 employees, annual phishing training showed no measurable effect, and embedded training only a minimal one (Ho et al. 2025). The model attributes this to the meso level (Section 4).
- Skepticism games mainly shift the response bias: participants reject more, including what is true (Modirrousta-Galian & Higham 2023; Hoes et al. 2024).
- Structured techniques work: premortem (Mitchell, Russo & Pennington 1989), Consider the Opposite (Lord, Lepper & Preston 1984), Lateral Reading (Wineburg & McGrew 2019). Debiasing training with feedback transfers to the field in individual studies (Morewedge et al. 2015; Sellier, Scopelliti & Morewedge 2019).
- Everyday feedback is one-sided: someone who declines never learns whether the request was legitimate (Hogarth 2001; Fetchenhauer & Dunning 2010).

### 6.2 Verification triggered by the action class

Content features such as spelling, tone or image quality lose their diagnosticity through generative AI (q towards 0). The model suggests a different rule: **verification depends on the action class, not on one's gut feeling about the sender.** Because θ is independent of the person, the rule can be applied without assessing the person.

| Trigger (action class) | Fixed response |
| --- | --- |
| Payment, account change, gift card purchase | call-back to a self-chosen, known number |
| Credentials, MFA code, password reset | never pass on; open the portal oneself |
| Change of rights or roles | approval by a second person |
| Disclosure of confidential data | verify permission with the data owner |
| Installing software, granting remote access | only via the official IT channel |
| Channel switch, secrecy, urgency | treat as a reason to verify, not as proof |

The table is a draft. The specific classes are to be defined per organization.

### 6.3 The quick procedure under time pressure

Example: a supposed manager urgently requests a payment. The question is not “Do I trust this person?”, but:

1. Verify identity via a known channel.
2. Verify permission for the payment request.
3. Verify the factual correctness of the payment.
4. If the evidence is insufficient, postpone or obtain further approvals.

**Time pressure is a reason for increased care, not proof of an attack.**

![The action triggers the verification, not the gut feeling](../../docs/figures/fig-07-quick-procedure.png)

*Figure 2: Quick procedure according to Section 6.3 · two decisions, three outcomes*

The first decision asks only about the type of action, not about how trustworthy the sender appears.

### 6.4 Guiding questions without time pressure

Five questions structure decisions without time pressure: What exactly am I supposed to believe or allow (action x, context c)? Who gains what from it (motivation)? What could go wrong (loss L)? What independent evidence exists (D, q, u)? What is the smallest justifiable next step (permission P)? The questions are a synthesis of premortem, Lateral Reading and Least Privilege, not a new invention. Check questions against false distrust complement them:

- What harmless explanation is there?
- Which observation would refute my suspicion?
- Would I evaluate the same cues in the same way for a likeable person?
- Do I know the claim from several independent sources, or have I just heard it often?
- Which of my beliefs colors this assessment?

### 6.5 Design principles for training

1. **Few triggers, fixed response.** If-then rules instead of general vigilance.
2. **Make verification cheap.** A call-back must be possible in under a minute and be socially accepted.
3. **Practice symmetrically.** Exercises contain legitimate and malicious cases, with feedback on both types of error.
4. **Measure discrimination,** not the rejection rate.
5. **Structure before vigilance.** Where an error is expensive, a control protects, not a person's attention.
6. **Limit friction.** Every rule consumes compliance budget (Beautement, Sasse & Wonham 2008). Too many rules produce circumvention and security fatigue (Stanton et al. 2016).
7. **Role and norm instead of appeal.** Every action class has a named verification role, and the team's verification rate is visible (Sections 4.2 and 4.4).

These principles are derived from the model and the literature. Their effectiveness as a package is untested (hypothesis H12).

### 6.6 Metrics

| Metric | Meaning |
| --- | --- |
| Discriminability d′ | distinguishing legitimate from malicious requests |
| Criterion c | general tendency to reject |
| Reporting rate and reporting time | share and speed of reported attacks |
| Verification rate per action class | share of triggered cases with actual verification |
| Time spent per verification | friction |
| Calibration (Brier score) | agreement between confidence and hit rate |
| Verification coverage C per action class | share of cases with at least one independent verification, measured per team (Section 4.2) |
| Assumed detection rate τ_I | how strongly employees leave verification to the institution (Section 4.3) |

### 6.7 Decision logs

For rare, consequential decisions, a short log helps.

- **Before:** expectation, available evidence, own confidence in percent, possible beliefs.
- **At the decision:** rights granted, risk accepted.
- **After:** actual course of events, relevant cues, false assumptions, truly independent information.
- **Learning:** Was the decision methodologically sound, regardless of the outcome? Did repetition influence the assessment?

The log should also track declined cases in order to avoid the learning trap (Section 4.6). **A good decision can turn out badly. A good outcome does not prove a good decision.**

## 7. Trust dimensions and security objectives

The model uses four core dimensions of trustworthiness: ability (competence), benevolence, integrity and predictability (Mayer et al. 1995, plus predictability). **The four trust dimensions do not cover the security objectives confidentiality, integrity and availability; they complement them.** The dimensions describe the actor B, the security objectives the asset. This section is a derivation from the model and has not yet been empirically tested (hypothesis H15).

### 7.1 Security objectives as types of loss

ISO/IEC 27000:2018 defines confidentiality, integrity (accuracy and completeness) and availability (accessible and usable on demand by an authorized entity). FIPS 199 and the BSI IT-Grundschutz Compendium use the same three basic values. All three allow further security objectives such as authenticity and non-repudiation; FIPS 199 counts them as part of integrity, the BSI groups them under *Verbindlichkeit*. **Whether authenticity is a security objective in its own right is not answered consistently by the standards** (Section 7.5).

Parker (1998) extended the triad to six elements, among them authenticity and utility. His example for utility: data are encrypted and the key is lost; the data are present, unchanged and confidential, but unusable.

FIPS 199 categorizes by the expected loss, not by the probability of an attack; the protection requirements assessment of IT-Grundschutz likewise asks about the loss. **Security objectives describe the loss side.** Who attacks, with what intent and capability, lies in threat modeling.

### 7.2 Two axes instead of one coverage

The trust dimensions are characteristics of B and determine how likely B is to meet an expectation: the actor side of risk. The security objectives name the respects in which an asset can be damaged. The vulnerability that Rousseau et al. (1998) and Mayer et al. (1995) describe as the core of trust is recorded in asset management not as willingness but as loss L.

Core assumption G1 already contains this separation: the loss depends on scope of action P and vulnerability L, not on the level of trust. A vulnerability arises when a positive expectation (the dimension axis) meets an exploitable scope of action with its loss (the security-objective axis) (long version, Section 8.1).

Both models together span a matrix. The rows are the dimensions k, the columns the security objectives z. A cell holds the risk that B fails in dimension k and that security objective z is violated as a result:

```math
\text{Risk}_{k,z} \approx \left(1 - E^{\text{norm}}_{k}\right)\cdot \mu_{k,z}\cdot L_{z}(P)
```

E is the expected trust in dimension k, μ(k,z) the mapping strength (Section 7.6), and L(P) the maximum loss to security objective z that B can cause with the granted scope of action P. **Without scope of action, L(P) = 0, and the risk vanishes, no matter how low the trust.** This is G1 in cell form. “B is benevolent but incompetent in handling keys” is a different cell from “B is competent but not benevolent, and passes data on.” Both violate confidentiality, but they require different countermeasures. The formula has the same structure as the verification rule, broken down by dimension and security objective.

### 7.3 The pairs and their limits

**Benevolence and confidentiality (strong).** B does not use my information against me; confidentiality is the loss side of the same expectation.

**Integrity and data integrity (strong).** B falsifies nothing, tells the truth about the state of the asset and is accountable; accountability links the pair to *Verbindlichkeit* (BSI) and non-repudiation.

**Predictability and availability (strong).** The service is there when it is needed; FIPS 199 itself uses the word “reliable” for availability.

**Integrity and confidentiality (weak).** Secrecy can be a commitment, but only where confidentiality has been agreed.

**Competence and all three (weak), without a counterpart of its own.** An incompetent B leaks by accident, corrupts through errors, causes outages, but competence has no column of its own in the triad. **CIA presupposes that the system does the right thing and only measures whether it remains undisturbed while doing so.**

Two observations sharpen the mapping. *False friend:* as a dimension, integrity means a person's adherence to principles; as a security objective it means that data remain unaltered. This paper therefore speaks of integrity (dimension) and data integrity (security objective). *Intent and error:* competence and predictability mainly explain unintended losses and are close to safety; benevolence and integrity explain intended losses and are close to security and threat modeling. This is consistent with S17: competence errors and deception lie on different rows of the matrix.

### 7.4 Competence without a counterpart: utility

If competence has no security objective, the question arises which one would correspond to it. The answer is Parker's utility: the result is present, unchanged and confidential, but unusable. That is the typical damage of missing competence. In ISO/IEC 27000 and in IT-Grundschutz, utility is not a security objective but a given value. **Utility is an input to the protection requirements assessment, not an object of protection.**

In practice, an attack on utility is usually represented through availability, as with ransomware. The mapping breaks down where the result is available and unchanged but inadequate from the start, such as wrong advice or a correctly implemented but wrong specification.

This yields a demarcation criterion. **Security models presuppose a target state and protect it against deviation. Competence concerns whether the target state is reached at all.** The third verification question, factual correctness, asks exactly this. In Chen's (2021) four-place relation, utility means that the action actually serves its goal. For AI agents, utility becomes a risk dimension in its own right (long version, Section 13.6, hypothesis H15c); this is treated in Paper 3 (Rumpf 2026c).

### 7.5 Authenticity as an anchor

In extended models authenticity is a security objective in its own right (Parker 1998; ISO/IEC 27000:2018); in others it is part of integrity (FIPS 199; BSI 2023). For the trust model a third reading is more fruitful: **authenticity is not the counterpart of one dimension but the anchor beneath the entire trust profile.** Before any dimension is assessed, one thing must be settled: is B really B?

Data integrity concerns the content (unchanged?), authenticity the origin (from whom?), which is a question of whom A trusts. Authenticity therefore belongs on the actor axis; in the model it is the edge attribution of the identity question. Impersonation is the attack in which an attacker inherits the evidence r of another node. **Whoever takes over the identity takes over not one dimension but the whole profile.** In CEO fraud, the attacker borrows the profile of the real executive. No security objective is violated by this alone; whether a loss occurs is decided by the requested action with its scope P and loss L. This is why the threshold rule starts from the action, not the person. The Zero Trust requirement to re-verify identity before every session (NIST SP 800-207) secures this anchor, not an individual cell.

### 7.6 The matrix

Each cell pairs a guiding question with a typical damage; for example, competence × utility asks “Can B produce the right result?” (damage: plausible but wrong). The full cell table is in the long version (Table 13.1); Table 1 gives the mapping strengths.

| Dimension | Confidentiality | Data integrity | Availability | Utility | Type of loss |
| --- | --- | --- | --- | --- | --- |
| Competence | weak | weak | weak | **strong** | error |
| Benevolence | **strong** | weak | weak | weak | intent |
| Integrity | weak | **strong** | weak | weak | intent |
| Predictability | weak | weak | **strong** | weak | fluctuation |
| Authenticity | – | – | – | – | anchor beneath all rows |

*Table 1: Mapping strength μ(k,z) · ratings are reasoned assumptions, not measured values*

![Three dimensions have a security objective, competence needs a fourth](../../docs/figures/fig-10-security-objectives.png)

*Figure 3: Trust dimensions and security objectives according to Sections 7.3 to 7.5 (and long version, Section 13.6) · strong and weak mappings, authenticity as an anchor*

The four strong mappings lie on the diagonal. Authenticity is not a fifth row but the condition that all four rows are actually attributed to B.

### 7.7 Implications

**For risk assessment.** A risk assessment that considers only security objectives tacitly presupposes competence and authenticity; a trust assessment without security objectives remains unclear about what is at stake.

**For training.** The quick procedure begins with identity, and the matrix supplies the reason: whoever takes over the identity takes over the whole profile. The first verification question is therefore always “Is B really B?” via an independent channel, before any dimension is assessed.

**For acceptance of agent results.** If several people share the acceptance of agent results, this verification, too, needs a named role (Section 4.2).

## 8. Security rules ranked by loss

Twenty-four concrete rules follow from the model (long version, Chapter 14). Many are known as good practice, such as Zero Trust, least privilege and separation of duties. **The model's contribution is a common justification, a ranking by size of the loss and a calculation rule for re-verification intervals.** The rules are derivations and, as a package, have not been empirically tested.

### 8.1 Permission and decision

| No. | Rule | Follows from | Implementation (examples) |
| --- | --- | --- | --- |
| S1 | Permissions depend on the action, not on the person. | threshold θ is independent of the person | approval levels per action class and amount |
| S2 | Identity, authorization and correctness are verified separately. | three separate evidence questions | payment approval checks sender, signing authority and invoice separately |
| S3 | High standing and long membership do not replace control. | loss grows with P and L, not with trust (G1) | four-eyes principle for management too |
| S4 | For actions with a very high loss, personal trust is never sufficient. | θ close to 1 cannot be reached with u_min > 0 | second independent approval, technical limits |
| S19 | With agents, the result is checked for utility per task, not just the system for availability and integrity. | competence has no counterpart in the CIA triad | acceptance criteria per task type, samples of re-checked results, utility as a fourth column of the protection requirements assessment |

S19 concerns agents and is treated in Paper 3 (Rumpf 2026c). In S4, u_min is the lower bound of uncertainty under temporal decay (long version, Section 4.3). S2 hits the core of business email compromise, with reported losses of about USD 2.77 billion in 2024 (FBI IC3 2024).

### 8.2 Evidence and channels

| No. | Rule | Follows from | Implementation (examples) |
| --- | --- | --- | --- |
| S5 | A confirmation via the same channel is not a second piece of evidence. | D = 1 yields n_eff = 1 | call-back via a self-chosen number, never via details from the request |
| S6 | A majority counts only if independent. | n_eff is bounded by 1 / D | de-duplicate ratings, reports and agent votes by origin |
| S7 | Content features no longer serve as proof of authenticity. | diagnosticity q tends to 0 as generation costs do | training on action triggers instead of typos or the sound of a voice |
| S8 | Only costly signals count as proof. | q measures forgery costs | signatures, proofs of possession, pre-agreed code words |
| S9 | The evidence account itself is an object of protection. | manipulation of the model | tamper-proof logs with provenance per entry |

### 8.3 Time and context

| No. | Rule | Follows from | Implementation (examples) |
| --- | --- | --- | --- |
| S10 | Trust ages and must be renewed. | temporal decay λ, re-verification interval t* | short-lived credentials, recertification of rights, locking of dormant accounts |
| S11 | Riskier rights are verified more often. | t* decreases with smaller u_max | staggered intervals per risk class |
| S12 | Trust from one domain does not justify rights in another. | evidence is context-specific | role separation; raising the verification level on a change of context |
| S13 | Trust is not transitive; chains are limited. | discounting operator | verify suppliers and subcontractors individually, limit delegation depth |

λ, t* and the discounting operator are derived in the long version (Sections 4.3, 4.6, 10.4).

### 8.4 People and organization

| No. | Rule | Follows from | Implementation (examples) |
| --- | --- | --- | --- |
| S14 | Verifications must be cheap, otherwise they do not happen. | verification rule K < τ·(1 − E)·L | call-back directory, report button, fixed point of contact |
| S15 | Structure beats vigilance. | low effect of awareness training (Ho et al. 2025) | technical locks and approvals for high-risk actions |
| S16 | False distrust is measured as a cost factor. | Γ < 0 is an error just like Γ > 0 | rate of rejected legitimate requests, time spent per verification |
| S17 | Errors and deception are treated differently. | conditional asymmetry | mis-clicks lead to support, not sanctions; deception leads to immediate, broad withdrawal |
| S18 | After an attack wave, thresholds are raised selectively for weakly evidenced edges. | ΔE = u·Δa | stricter verification for new contacts and changed master data instead of for everyone |

S17 has a practical reason: whoever is punished for a mis-click does not report it, and the organization loses evidence. This justification is an assumption and is to be checked.

### 8.5 Groups and organization

| No. | Rule | Follows from | Implementation (examples) |
| --- | --- | --- | --- |
| S20 | Every action class has a named verification role, no “someone checks”. | diffusion of responsibility, verification coverage C (Section 4.2) | verifier named in the approval process; deputy rule |
| S21 | Second verifiers verify independently: different channel, own information, own responsibility. | D of the verifiers (Section 4.2) | second approval sees the request, not the justification of the first approval |
| S22 | The security institution makes visible what it does not catch. | protection delegation, τ_I (Section 4.3) | quarterly figure of attacks that got through; notice on filtered mails: “Filtered does not mean verified” |
| S23 | Verification rates are measured per team and communicated as a norm, never per person. | descriptive norm (Section 4.4); performance monitoring (Section 12) | team dashboard; no individual evaluation |
| S24 | New relationships get higher thresholds until individual evidence is available. | swift trust, u close to 1 (Section 4.5, V9) | second approval for first payments to new suppliers and for master data changes |

S22 carries a risk: if the error rate is communicated without context, τ_I tips into undertrust (V22). The figure therefore belongs next to the verification rule for the individual, not on its own.

### 8.6 The four most important rules

If only four rules can be introduced:

1. **S1 with S5:** For a short list of risky actions, a verification via a second, self-chosen channel always applies.
2. **S10:** Every permission has an expiry date, staggered by risk.
3. **S14:** The verification takes less than a minute and is explicitly welcome.
4. **S20:** A named person verifies. Without this rule the other three come to nothing, because the verification is provided for but carried out by no one.

This selection follows from the ratio of size of the loss to effort in the model. It is a recommendation, not a finding.

## 9. Core assumptions, hypotheses and predictions

### 9.1 Core assumptions

Two of the four core assumptions of the long version carry this paper. They are considered established after the literature review.

| ID | Core assumption | Reference in the model | Key evidence |
| --- | --- | --- | --- |
| G1 | The loss from an abuse of trust depends on the scope of action granted and the vulnerability, not on the level of trust. | long version, Sections 6.2 and 8.1 | Mayer et al. 1995; Saltzer & Schroeder 1975; ACFE 2024 |
| G4 | In groups, evidence intake, interpretation and verification behavior are formed socially: Visible judgments of others shift one's own judgments, decisions of others are adopted as evidence, and the willingness to act decreases with the number of possible actors. | long version, Chapter 7 | Asch 1951; Bond & Smith 1996; Bikhchandani et al. 1992; Darley & Latané 1968; Fischer et al. 2011 |

### 9.2 Hypotheses

**H6 – Separate verifications.** Anyone who verifies identity, authorization and factual correctness separately and ties permissions to the size of the loss instead of to trust in the person makes fewer risky wrong decisions at a justifiable additional effort.

**H7 – Action-bound adversarial thinking.** Structured adversarial thinking bound to action classes improves discriminability in risky decisions. Generally increased skepticism only shifts the response bias and increases false distrust.

**H8 – Trainability under conditions.** Trust competence is trainable if the training conveys explicit rules, gives prompt feedback on both types of error and is repeated realistically. Without these conditions, effects remain small and short-lived. Additional condition: The group norm supports verification (Section 4.4); against the norm, individual training remains ineffective.

**H12 – Trigger-based training.** Training with only a few action triggers and a fixed, low-effort verification response lowers the success rate of social engineering attacks more than feature-based awareness training, without increasing the rejection of legitimate requests. The effect occurs only in combination with assigned verification roles and a visible team norm; as purely individual training it remains small (Section 4).

**H15 – Trust dimensions and security objectives.** The four trust dimensions and the security objectives of information security describe the same risk from two sides: The dimensions are properties of actor B and determine the probability of occurrence, the security objectives are properties of the asset and determine the type of loss. They form a matrix, not a mapping onto each other.

- **H15a – Three pairs, one gap.** Benevolence and confidentiality, integrity and data integrity, and predictability and availability are strong mappings. Competence has a weak effect on all three but has no counterpart in the CIA triad.
- **H15b – Authenticity as anchor.** Authenticity is not a counterpart to a dimension but the condition under which the trust profile is attributed to B. Impersonation invalidates the attribution of all rows of the matrix at once; whether a loss results still depends on scope of action P and loss L (G1).
- H15c (utility for agents) is treated in Paper 3 (Rumpf 2026c).

**H16 – Protection delegation.** The higher the perceived detection rate τ_I of the security institution, the less often employees carry out verification themselves, regardless of their knowledge of attack features. The calibration gap on the edge to the institution predicts click rates in phishing simulations better than results of awareness tests.

**H17 – Diffusion of responsibility in verifications.** Verification coverage C per action class decreases with the number of possible verifiers, provided no role is assigned. One named verification role achieves higher coverage than two unnamed ones.

H16 and H17 are two instances of one structure, perceived coverage by other nodes (Section 4.8). The decrease of coverage with n and its dependence on the loss L are derived there from the verification rule; that people presume coverage at all is imported (G4).

**H18 – Norms before knowledge.** The descriptive norm in the team (perceived verification rate of colleagues) predicts one's own verification behavior better than individual knowledge and than the prescribed rule.

**H19 – Visible gap instead of appeal.** If the security institution makes its error rate visible, τ_I decreases, and the verification rate rises more than after general awareness communication.

### 9.3 Evidence status

| ID | Status | Supporting sources | Limiting sources |
| --- | --- | --- | --- |
| H6 | conceptually strong, untested at the individual level | Lee & See 2004; ACFE 2024; FBI IC3 2024 | Beautement et al. 2008; Parasuraman & Manzey 2010 |
| H7 | contested | Mitchell et al. 1989; Lord et al. 1984 | Modirrousta-Galian & Higham 2023; Hoes et al. 2024; Levine 2014 |
| H8 | partly supported | Morewedge et al. 2015; Mellers et al. 2014; Fetchenhauer & Dunning 2010 | Hauch et al. 2016; Hogarth 2001; Ho et al. 2025 |
| H12 | untested | derived from H6 to H8 | Ho et al. 2025 shows low effect of previous trainings |
| H15 | conceptually grounded, untested | Mayer et al. 1995; Parker 1998; NIST AI 100-1 2023; OWASP 2025 | utility not established outside Parker; distinction from data integrity empirically blurred |
| H16 | untested; transfer; first clause partly supported | Peltzman 1975; Wilde 1982; Herley 2009; Zhang, Reithel & Li 2009 | τ_I measured only as perceived technical protection and intended compliance (Zhang et al. 2009), not per edge; the comparison with awareness tests is untested |
| H17 | mechanism well supported; n- and L-dependence derived (Section 4.8); transfer to verification coverage untested | Darley & Latané 1968; Fischer et al. 2011; Diekmann 1985; Brink, Eller & Gan 2015; Paravastu, Simmers & Anandarajan 2018 | security measurements concern reporting and intentions, not verification coverage; the danger moderator (Fischer et al. 2011) is consistent with V28 but manipulates danger, not the loss L of the model |
| H18 | mechanism well supported, transfer untested | Cialdini et al. 1990; Beautement et al. 2008 | norm effects are context-dependent |
| H19 | untested | derived from H16 and ΔE = u·Δa | risk of tipping into undertrust (V22) |

### 9.4 Operationalization

For each hypothesis, the following must be specified before testing: independent and dependent variables, confounders, measurement methods, expected direction and criteria for confirmation or refutation. The effectiveness hypotheses H6 to H8 and H12 need designs that measure effectiveness separately via discriminability and response bias. H15 is a structural hypothesis: it is tested by coding real incidents by dimension and security objective, not by an experiment. H16 to H19 are field hypotheses at team level; the dependent variable is verification coverage C, never the behavior of individuals.

### 9.5 Predictions

The following predictions are derivations from the equations of the model. They are predictions, not findings.

| No. | Prediction | Derivation | Testable by |
| --- | --- | --- | --- |
| V22 | After the first visible security incident, trust in IT tips from overtrust into undertrust, without an intermediate state. | u on A→I high, ΔE = u·Δa (Section 4.3) | survey on τ_I before and after incidents |
| V23 | Teams with high source dependence report attacks less often, although more people see them. | cascade: “If it were dangerous, someone would have reported it” | reporting rate against team size and source overlap |
| V24 | Four-eyes approvals with the same level of information hardly lower the error rate compared with a single approval. | D of the verifiers close to 1 (Section 4.2) | comparison of correlated and independent second approvals |
| V25 | New project and supplier relationships are overrepresented in incident data. | Swift Trust, V9 | incidents by relationship age |
| V26 | Contact with outside sources improves calibration in bubbles and worsens it in echo chambers. | u against d (Section 4.7) | separate measurement of u and d towards outside sources before contact |
| V27 | Awareness training without changes in roles and norms changes test results, not verification rates. | H12, H18 | test scores against measured verification coverage |
| V28 | Diffusion of responsibility is strongest for action classes with a low visible loss and weakest for a high visible loss: the drop in coverage from n = 1 to n = 4 is larger for routine mails than for large payments. | c_n = 1 − ρ^(1/(n−1)), ρ falls with L (Section 4.8) | coverage by n, crossed with action class |
| V29 | The effects of trust in the security institution and of the number of unassigned verifiers multiply: teams with a high τ_I and several unnamed verifiers show lower coverage than either factor alone predicts. | 1 − τ̂_O = (1 − τ_I)(1 − τ̂ĉ)^(n−1) (Section 4.8) | survey on τ_I crossed with role assignment, coverage per team |

The predictions are qualitative. Quantitative statements need estimated parameters per population and context.

## 10. Research agenda

### 10.1 Simulation scenarios

Four scenarios of the long version (Section 15.2) concern this paper:

- **Scenario 12.** Payment request under time pressure with and without a trigger rule (H12).
- **Scenario 14.** Team with n = 1, 2 and 4 possible verifiers, role assigned and not assigned, crossed with the loss L and with τ_I (H17, V24, V28, V29).
- **Scenario 15.** Protection delegation: τ_I assumed 0.99 versus actually 0.9, with and without a visible error rate (H16, H19, V22).
- **Scenario 16.** Two groups with the same E towards outside sources, one u-dominated (bubble), one d-dominated (chamber), under outside contact (V26).

The technical verification of a simulation is not an empirical validation of the psychological model. Further steps are a pilot training (H12) and a coding scheme for real incidents by dimension × security objective (H15; long version, Section 15.6).

### 10.2 Open practical questions

- Which trigger list is short enough to be followed and broad enough to protect?
- How much independent evidence is needed for which action class?
- How does a person recognize that their assessment rests on familiarity rather than evidence?
- How can τ_I be measured without the question itself triggering undertrust in the institution?
- Which team size and which role assignment maximize verification coverage C with acceptable friction?

How λ and u_max are set on a justified basis for agent systems is discussed in Paper 3 (Rumpf 2026c).

## 11. Limitations

- **Transfer.** Conformity, cascades and diffusion of responsibility are well supported in the laboratory and in the field. In security contexts they have been measured as reporting and compliance intentions (Zhang, Reithel & Li 2009; Brink, Eller & Gan 2015; Paravastu, Simmers & Anandarajan 2018), not as verification coverage per action class. H16 to H19 are transfers in that narrower sense; Section 4.8 states which part of H16 and H17 the model derives and which it imports.
- **Symmetric solution.** The derivation in Section 4.8 assumes that every potential verifier knows n, treats the others as alike, presumes their detection rate τ̂ and applies the verification rule as a threshold; the closed form is stated for τ̂ = 1. Habit and the social part of K are not in it.
- **Meso parameters.** τ_I, c_n and the descriptive norm can only be estimated in field studies. In simulations they are assumptions.
- **Verification rates per person are performance monitoring.** The metrics of this paper apply per team and action class, never per person (Section 12, rule S23).
- **An organization is not just a group.** Hierarchy, incentives and formal processes have additional effects not covered here.
- **Utility and demarcation.** Utility is hardly established outside Parker; neither ISO/IEC 27000 nor IT-Grundschutz lists it. Whether a result was never correct or was altered later is not always observable, for example with poisoned training data; there, cells overlap.
- **Mapping strengths rest on argument, not measurement.** Table 1 is an assumption. An empirical test, for example by coding real incidents by row and column, is still pending.
- **Inconsistent standards on authenticity.** The reading as an anchor is a proposal; FIPS 199 and the BSI assign it to integrity, Parker and ISO/IEC 27000 list it separately.
- **Untested rules.** The rules in Section 8 are derivations and untested as a package.

## 12. Ethics and law

The model serves self-reflection, training, simulation and the assessment of technical systems. **It does not serve the assessment of persons for decisions by third parties.**

- **Performance monitoring.** Verification rates and reporting rates per person constitute behavior and performance monitoring and in Germany are subject to works-council co-determination (German Works Constitution Act (BetrVG) § 87(1) no. 6). The metrics of this paper are therefore collected per team and action class (S23).
- **No per-person measurement.** The field hypotheses H16 to H19 use verification coverage C at team level as the dependent variable, never the behavior of individuals.

The legal classification is an initial assessment and does not replace a legal review.

## 13. Conclusion

Training that targets the individual's evaluation achieves little. This paper locates the reason at the meso level: groups act less on evaluation than on verification. Where several people could verify and no one is assigned, verification becomes a public good that is undersupplied. Where a security institution is presumed to filter, a rationally applied verification rule with a miscalibrated τ_I makes one's own verification seem pointless. Where verification counts as distrust, the descriptive norm makes it socially expensive.

Because the threshold for a permission depends on the action, not on the person, verification can be bound to a short list of action classes, made cheap and assigned to a named role. Trust dimensions and security objectives complement each other on two axes, with authenticity as the anchor. Many of the derived rules are known as good practice; the model adds a common justification and a ranking by size of the loss.

All of this is a derivation. The hypotheses H16 to H19 are transfers from social psychology, except for the parts that Section 4.8 derives from the verification rule, and H12 and H15 are untested. The appropriate next step is field studies at team level, not a claim of effectiveness. Trust is engineered in the sense that decisions that rest on trust can be structured, verified and improved.

## References

- Rumpf, J. (2026a). Trust is Engineered. Working paper, version 0.7 (draft). https://github.com/JoeRu/trust-is-engineered
- Rumpf, J. (2026b). Trust is Engineered: An Evidence Model of Trust, Distrust and the Calibration Gap. Preprint, version 0.1 (draft), Paper 1 of 3. Zenodo. https://doi.org/10.5281/zenodo.23810447
- Rumpf, J. (2026c). Engineering Calibrated Trust between Humans, Agents and Machines: Evidence Accounts, Decay and Re-verification. Preprint, version 0.1 (draft), Paper 3 of 3. Zenodo. https://doi.org/10.5281/zenodo.23813132
- ACFE (2024). Occupational Fraud 2024: A Report to the Nations.
- Allport, G. W. (1954). The Nature of Prejudice. Addison-Wesley. (to be checked)
- Asch, S. E. (1951). Effects of group pressure upon the modification and distortion of judgments. In Guetzkow (Eds.), Groups, Leadership and Men. Carnegie Press. (to be checked)
- Beautement, A., Sasse, M. A. & Wonham, M. (2008). The compliance budget. NSPW, 47–58.
- Bikhchandani, S., Hirshleifer, D. & Welch, I. (1992). A Theory of Fads, Fashion, Custom, and Cultural Change as Informational Cascades. Journal of Political Economy, 100(5), 992–1026. (to be checked)
- Bond, C. F. & DePaulo, B. M. (2006). Personality and Social Psychology Review, 10(3), 214–234.
- Bond, R. & Smith, P. B. (1996). Culture and conformity: A meta-analysis of studies using Asch's line judgment task. Psychological Bulletin, 119(1), 111–137. (to be checked)
- Brink, A., Eller, C. K. & Gan, H. (2015). Reporting fraud: An examination of the bystander effect and evidence strength. Advances in Accounting Behavioral Research, 125–154. https://doi.org/10.1108/S1475-148820150000018004 (secondary citation)
- BSI (2023). IT-Grundschutz-Kompendium, Edition 2023, Glossar. Bundesamt für Sicherheit in der Informationstechnik. (wording on authenticity and *Verbindlichkeit* to be checked)
- Chen, M. (2021). Trust and Trust-Engineering in Artificial Intelligence Research: Theory and Praxis. Philosophy & Technology, 34, 1429–1447. https://doi.org/10.1007/s13347-021-00465-4 (checked against full text)
- Cialdini, R. B., Reno, R. R. & Kallgren, C. A. (1990). A focus theory of normative conduct. Journal of Personality and Social Psychology, 58(6), 1015–1026. (to be checked)
- Darley, J. M. & Latané, B. (1968). Bystander intervention in emergencies: Diffusion of responsibility. Journal of Personality and Social Psychology, 8(4), 377–383. (to be checked)
- Diekmann, A. (1985). Volunteer's Dilemma. Journal of Conflict Resolution, 29(4), 605–610. https://doi.org/10.1177/0022002785029004003 (to be checked)
- Edmondson, A. (1999). Psychological safety and learning behavior in work teams. Administrative Science Quarterly, 44(2), 350–383. (to be checked)
- FBI Internet Crime Complaint Center (2024). Internet Crime Report 2024.
- Fetchenhauer, D. & Dunning, D. (2010). Why so cynical? Psychological Science, 21(2), 189–193.
- Fischer, P. et al. (2011). The bystander-effect: A meta-analytic review on bystander intervention in dangerous and non-dangerous emergencies. Psychological Bulletin, 137(4), 517–537. (to be checked)
- German Works Constitution Act (Betriebsverfassungsgesetz, BetrVG), § 87(1) no. 6.
- Grossklags, J., Christin, N. & Chuang, J. (2008). Secure or insure? A game-theoretic analysis of information security games. WWW '08, 209–218. https://doi.org/10.1145/1367497.1367526 (secondary citation)
- Hauch, V., Sporer, S. L., Michael, S. W. & Meissner, C. A. (2016). Communication Research, 43(3), 283–343.
- Herley, C. (2009). So Long, and No Thanks for the Externalities: The Rational Rejection of Security Advice by Users. NSPW, 133–144. (to be checked)
- Ho, G., Mirian, A., Luo, E. et al. (2025). Understanding the Efficacy of Phishing Training in Practice. IEEE Symposium on Security and Privacy.
- Hoes, E., Aitken, B., Zhang, J., Gackowski, T. & Wojcieszak, M. (2024). Nature Human Behaviour, 8, 1545–1553.
- Hogarth, R. M. (2001). Educating Intuition. University of Chicago Press.
- ISO/IEC 27000:2018. Information technology – Security techniques – Information security management systems – Overview and vocabulary. (definitions to be checked against the text of the standard)
- Janis, I. L. (1972). Victims of Groupthink. Houghton Mifflin. (to be checked)
- Jøsang, A. (2016). Subjective Logic. Springer.
- Jøsang, A. & Ismail, R. (2002). The Beta Reputation System. 15th Bled eConference.
- Karau, S. J. & Williams, K. D. (1993). Social loafing: A meta-analytic review and theoretical integration. Journal of Personality and Social Psychology, 65(4), 681–706. https://doi.org/10.1037/0022-3514.65.4.681 (to be checked)
- Latané, B. & Darley, J. M. (1970). The Unresponsive Bystander: Why Doesn't He Help? Appleton-Century-Crofts. (to be checked)
- Lee, J. D. & See, K. A. (2004). Human Factors, 46(1), 50–80.
- Levine, M. & Crowther, S. (2008). The responsive bystander: How social group membership and group size can encourage as well as inhibit bystander intervention. Journal of Personality and Social Psychology, 95(6), 1429–1439. (to be checked)
- Levine, T. R. (2014). Journal of Language and Social Psychology, 33(4), 378–392.
- Lord, C. G., Lepper, M. R. & Preston, E. (1984). Journal of Personality and Social Psychology, 47(6), 1231–1243.
- Lorenz, J., Rauhut, H., Schweitzer, F. & Helbing, D. (2011). How social influence can undermine the wisdom of crowd effect. PNAS, 108(22), 9020–9025. (to be checked)
- Marques, J. M., Yzerbyt, V. Y. & Leyens, J.-P. (1988). The “black sheep effect”. European Journal of Social Psychology, 18(1), 1–16. (to be checked)
- Mayer, R. C., Davis, J. H. & Schoorman, F. D. (1995). An Integrative Model of Organizational Trust. Academy of Management Review, 20(3), 709–734.
- Mellers, B. et al. (2014). Psychological Science, 25(5), 1106–1115.
- Meyerson, D., Weick, K. E. & Kramer, R. M. (1996). Swift trust and temporary groups. In Kramer & Tyler (Eds.), Trust in Organizations. Sage. (to be checked)
- Mitchell, D. J., Russo, J. E. & Pennington, N. (1989). Journal of Behavioral Decision Making, 2(1), 25–38.
- Modirrousta-Galian, A. & Higham, P. A. (2023). Journal of Experimental Psychology: General, 152(9), 2411–2437.
- Morewedge, C. K. et al. (2015). Policy Insights from the Behavioral and Brain Sciences, 2(1), 129–140.
- Nguyen, C. T. (2020). Echo Chambers and Epistemic Bubbles. Episteme, 17(2), 141–161. (to be checked)
- NIST (2004). FIPS PUB 199: Standards for Security Categorization of Federal Information and Information Systems.
- NIST (2023). Artificial Intelligence Risk Management Framework (AI RMF 1.0). NIST AI 100-1. https://doi.org/10.6028/NIST.AI.100-1
- OWASP (2025). OWASP Top 10 for LLM Applications 2025 (LLM06 Excessive Agency, LLM09 Misinformation). OWASP Foundation.
- Parasuraman, R. & Manzey, D. H. (2010). Human Factors, 52(3), 381–410.
- Paravastu, N., Simmers, C. A. & Anandarajan, M. (2018). Non-compliant mobile device usage and information systems security: A bystander theory perspective. International Journal of Information Systems and Social Change, 9(1), 1–25. https://doi.org/10.4018/IJISSC.2018010101 (secondary citation)
- Parker, D. B. (1998). Fighting Computer Crime: A New Framework for Protecting Information. Wiley. (page number for utility to be checked)
- Peltzman, S. (1975). The Effects of Automobile Safety Regulation. Journal of Political Economy, 83(4), 677–725. (to be checked)
- Pettigrew, T. F. & Tropp, L. R. (2006). A meta-analytic test of intergroup contact theory. Journal of Personality and Social Psychology, 90(5), 751–783. https://doi.org/10.1037/0022-3514.90.5.751 (secondary citation)
- Rose, S. et al. (2020). Zero Trust Architecture. NIST SP 800-207.
- Rousseau, D. M., Sitkin, S. B., Burt, R. S. & Camerer, C. (1998). Not so different after all. Academy of Management Review, 23(3), 393–404.
- Sagan, S. D. (2004). The problem of redundancy problem: Why more nuclear security forces may produce less nuclear security. Risk Analysis, 24(4), 935–946. https://doi.org/10.1111/j.0272-4332.2004.00495.x (to be checked)
- Saltzer, J. H. & Schroeder, M. D. (1975). Proceedings of the IEEE, 63(9), 1278–1308.
- Sellier, A.-L., Scopelliti, I. & Morewedge, C. K. (2019). Psychological Science, 30(9), 1371–1379.
- Sommerfeld, R. D., Krambeck, H.-J., Semmann, D. & Milinski, M. (2007). PNAS, 104(44), 17435–17440.
- Stanton, B. et al. (2016). Security fatigue. IT Professional, 18(5), 26–32.
- Varian, H. (2004). System reliability and free riding. In Camp & Lewis (Eds.), Economics of Information Security, 1–15. Springer. https://doi.org/10.1007/1-4020-8090-5_1 (secondary citation)
- Wilde, G. J. S. (1982). The theory of risk homeostasis: Implications for safety and health. Risk Analysis, 2(4), 209–225. https://doi.org/10.1111/j.1539-6924.1982.tb01384.x (secondary citation)
- Wineburg, S. & McGrew, S. (2019). Teachers College Record, 121(11).
- Zhang, J., Reithel, B. J. & Li, H. (2009). Impact of perceived technical protection on security behaviors. Information Management & Computer Security, 17(4), 330–340. https://doi.org/10.1108/09685220910993980 (secondary citation)
