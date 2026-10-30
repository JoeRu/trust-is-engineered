# Trust is Engineered: An Evidence Model of Trust, Distrust and the Calibration Gap

> **DRAFT.** Work in progress, not peer reviewed and not empirically validated. Derived from the working paper *Trust is Engineered* v0.6 ([long version](../../docs/trust-is-engineered.md)); identifiers and evidence status follow it.

Johannes Rumpf ([ORCID 0009-0001-8675-0608](https://orcid.org/0009-0001-8675-0608)) · Version 0.1 · 18 October 2026

## Abstract

Generative AI lowers the cost of producing convincing content, so features of the content lose their value as evidence of trustworthiness. This paper proposes a dynamic, context-sensitive model of trust and distrust under uncertainty. Trust is represented as a directed graph whose edges carry, per context and dimension, an opinion of trust b, distrust d and uncertainty u with a base rate a, following Subjective Logic. Two evidence accounts for positive and negative evidence are updated with a forgetting factor, so that trust without new evidence decays not to zero but to ignorance. Repetitions from dependent sources count only as an effective sample. The model keeps a normative, evidence-appropriate account separate from a descriptive account that also contains familiarity and belief-colored interpretation. Their difference, the calibration gap Γ, is the central derived quantity: Γ > 0 is unjustified trust, Γ < 0 unjustified distrust. A decision layer separates identity, authorization and factual correctness and derives a threshold for permissions from the loss and benefit of an action. Social engineering techniques are read as operations on model quantities; attacks fall into two classes, abuse attacks and calibration attacks. The paper states three core assumptions, eight hypotheses and one sub-hypothesis with their evidence status and twenty-one derived, untested predictions. The model is a research concept and has not been empirically tested.

**Keywords:** trust; distrust; calibration; Subjective Logic; evidence model; social engineering; illusory truth effect

Identifiers G (core assumption), H (hypothesis), V (prediction) and S (rule) follow the long version [Rumpf 2026, v0.6] so that they stay stable across papers.

## 1. Introduction

### 1.1 Trust in an AI-shaped world

AI slop, deepfakes, love scams and AI-generated identities change the conditions under which people trust information and other entities. **Content alone no longer determines credibility.** What becomes relevant is where it comes from, how it was created and through which channel it arrives. Is a person on LinkedIn the one they claim to be? Is a job offer, an invitation or a product review authentic? Does an impressive work result show competence or merely a convincing AI output? What does it mean when many seemingly independent sources repeat the same claim? May an AI agent that identifies itself correctly also trigger the requested action?

The change acts at the macro level (public sphere, institutions, information quality), at the meso level (teams, departments, organizations in which security decisions are actually made) and at the micro level (individual trust decisions). This paper develops the model at the micro level, as edges between entities. The meso level is treated in Paper 2 (Rumpf, in preparation).

### 1.2 Shift in the assessment of work

Generative AI lowers the cost of producing a convincing result. A signal is only credible if it is costly for deceivers (Spence 1973). **Features of the result therefore lose informative value.** Weight shifts to the traceable process of creation, verifiable evidence and the sources used.

### 1.3 Two application problems

The model is a theoretical framework for two practical problems. Problem A is training people: how do people learn to recognize abuse of trust such as phishing and social engineering with little effort and a high hit rate, without rejecting legitimate requests across the board? Problem B is integrating machines: how can trust between human and agent, and between machines, be established and verified on a recurring basis? **Both problems have the same structure: an entity must decide which action it allows another entity under incomplete evidence.** This paper presents the common model. Application A is treated in Paper 2 (Rumpf, in preparation), application B in Paper 3 (Rumpf, in preparation).

### 1.4 Research questions

This paper addresses three research questions of the long version:

1. How can trust between people, groups, institutions and technical systems be modeled in a context-dependent, dynamic way and under uncertainty?
2. What deviation exists between actual (descriptive) and evidence-appropriate (normative) trust formation, and how do attackers exploit it?
3. What predictions does the model allow about distrust, context transfer, loss over time, and the effect of news and global events?

The descriptive and the normative goal remain methodologically separate. **Their difference is the central object of investigation.**

The contribution is a graph-based evidence model that keeps trust, distrust and uncertainty separate, adds temporal decay and source dependence, separates a normative from a descriptive account and defines their difference Γ as the calibration gap. Attacks are read as operations on model quantities. Sections 5, 7 and 10 contain derivations of their own from the model. They are model statements and have not been empirically tested.

## 2. Related work

The model builds on integrative definitions of trust that tie it to vulnerability and separate it from risk taking (Rousseau et al. 1998; Mayer et al. 1995), and on the view that trust and distrust are separate dimensions (Lewicki et al. 1998). Its formal core is taken from Subjective Logic and the Beta Reputation System (Jøsang 2016; Jøsang & Ismail 2002). It draws on research on trust in automation (Lee & See 2004), on the illusory truth effect (Hasher et al. 1977) and on the neglect of correlated sources (Enke & Zimmermann 2019), and it positions itself against trust engineering in the sense of Chen (2021). A detailed comparison with prior work is given in the accompanying document [related-work.md](related-work.md).

## 3. Conceptual and theoretical foundations

### 3.1 Definition of trust

**Trust is a subjective, context-dependent expectation about the behavior of an entity under uncertainty, combined with the willingness to make oneself vulnerable.** The definition follows Rousseau, Sitkin, Burt & Camerer (1998) and Mayer, Davis & Schoorman (1995). Trust is a three-place relation: A trusts B with respect to X (Hardin 2002). **The goal is not more trust, but trust in what is trustworthy** (O'Neill 2002).

Five quantities are kept separate:

1. Trust assessment: How positive is my expectation?
2. Evidential certainty: How well is it justified?
3. Vulnerability: What loss does a wrong expectation cause?
4. Willingness to act: What risk do I take?
5. Permission: What scope of action do I actually grant?

Mayer et al. (1995) already separate Trust from Risk Taking in Relationship. The model adopts this separation as a core assumption.

### 3.2 Trust and distrust are two quantities

**Distrust is not the absence of trust.** Lewicki, McAllister & Bies (1998) describe both as separate dimensions. Reimann, Schilke & Cook (2017) find different origins: **trust is partly heritable, distrust follows socialization**. This yields three distinguishable states that a single scalar equates:

| State | Trust b | Distrust d | Uncertainty u | Example |
| --- | --- | --- | --- | --- |
| Ignorance | low | low | high | unknown sender |
| Ambivalence | high | high | low | capable colleague with a known conflict of interest |
| Justified trust | high | low | low | long-standing, verified supplier |

![Ignorance and ambivalence have the same expected value, but a different position](../../docs/figures/fig-01-states.png)

*Figure 1: Three states compared · illustrative values, base rate a = 0.5*

Ignorance and ambivalence yield the same expected value. They differ in uncertainty: under ignorance, a single event changes a lot; under ambivalence, little. The same separation distinguishes the epistemic bubble (u toward outside sources) from the echo chamber (d toward outside sources); the two call for opposite countermeasures (long version, Section 7.8).

### 3.3 Giving trust and earning trust

Initial trust is an advance without direct experience. Experience-based trust arises from observations. In the model, advance trust corresponds to the prior, experience to the accumulated evidence. **High initial trust never means high evidential certainty.** The developmental phases according to Lewicki & Bunker (1996) (calculus-, knowledge- and identification-based trust) and initial formation according to McKnight, Cummings & Chervany (1998) are adopted as a frame of reference.

### 3.4 Dimensions of trustworthiness

Trustworthiness is often described through many individual traits, such as honesty, reliability, openness, respect and responsibility. These traits are not independent. The model uses four core dimensions.

| Core dimension | Guiding question | Assigned individual traits |
| --- | --- | --- |
| Ability (competence) | Can B do it? | competence |
| Benevolence | Does B wish me well? | benevolence, respect |
| Integrity | Does B adhere to rules and truth? | honesty, integrity, responsibility, openness |
| Predictability | Does B behave consistently? | reliability |

The assignment follows Mayer et al. (1995) and McKnight, Choudhury & Kacmar (2002). The ABI factors correlate highly but each has a distinct effect (Colquitt, Scott & LePine 2007). The factor structure is to be tested by confirmatory factor analysis. **Competence and integrity must at least remain separate, because violations act differently** (Section 5.4). For machines and agents, the dimensions correspond to performance, purpose and process according to Lee & See (2004).

### 3.5 Positioning: trust engineering in Chen (2021)

The term trust engineering is already used by Chen (2021), though with a different goal. **Chen designs the trustee; this model designs the trust decision.** The two approaches complement each other. Chen describes trust as a four-place relation R(A, B, φ, G): A trusts B with respect to an action φ that serves a goal G. This extends the three-place relation from Section 3.1 by the goal. In this model, the goal is contained in the benefit N and loss L of the action (Section 7.2).

| Statement in Chen (2021) | Counterpart in this model |
| --- | --- |
| Threshold condition: trust exists when the attributed probability m reaches a threshold n | threshold rule in 7.2; here the threshold follows from the loss and benefit of the action |
| In such approaches, the value 0.5 stands for uncertainty | b, d and u separate ignorance from ambivalence (3.2) |
| Reliance is not yet trust: malfunction is followed by disappointment, a breach of trust by a feeling of betrayal; trust presupposes a normative expectation | only partly represented: integrity violations with deception weigh more heavily (5.4) |
| Distrust can be the appropriate default stance, depending on environment, domain and consequences | base rate a per context; new agents start with u = 1 (long version, 10.2) |
| The trustee is more an AI ecosystem of developers, operators and users than a single system | provider, model and operator as separate nodes; attestation (long version, 10.2, 10.3) |
| Trust signals via outward appearance exploit weaknesses of judgment and do not make the system more trustworthy | signals without diagnosticity (q close to 0) only raise the descriptive account and enlarge Γ (5.8, 8.4) |
| Appreciation by trustors as part of the reward function of learning agents | no counterpart; such ratings would here be evidence to be weighted by independence D (5.7) |

This implies a limit. In Chen's terms, this model mainly describes calibrated reliance and the permission derived from it. It does not specifically represent normative expectations and reactions such as the feeling of having been betrayed. It leaves open whether agents can be trustees in the full sense.

## 4. Trust as a directed, context-dependent graph

### 4.1 Basic model

Trust is modeled as a directed graph G = (V, E). V is the set of entities, E the set of directed relationships. Entities are persons, groups, organizations, institutions, technical systems and AI agents. **The relationship is directed, not symmetric, and changes over time.** A can trust B strongly while B trusts A little. For technical objects without an assessment of their own, the relationship is one-sided. Agents that verify permissions themselves maintain edges of their own.

![Trust is directed and holds per context](../../docs/figures/fig-02-graph.png)

*Figure 2: Example graph · four entities, directed edges per context*

Between the same two entities there are several edges: one per direction and per context. Membership is an edge type of its own. Each edge carries, per context c and dimension k, an opinion instead of a scalar:

```math
\omega_{A\to B,c,k} = (b,\; d,\; u,\; a), \qquad b + d + u = 1
```

b is trust, d distrust, u uncertainty, a the base rate (prior). The representation follows Subjective Logic (Jøsang 2016).

### 4.2 Context

**Trust is not universal**: I can trust a person's professional judgment but not lend them money. The context is defined as a triple:

```math
c = (\text{task domain},\; \text{vulnerability type},\; \text{relationship type})
```

| Component | Values (examples) |
| --- | --- |
| Task domain | professional judgment, payment approval, data access, code execution, care |
| Vulnerability type | financial, informational, physical, reputational, emotional |
| Relationship type | particular (known), generalized (stranger), institutional, technical |

The distinction between particular, generalized and institutional is empirically supported (Delhey, Newton & Welzel 2011; Freitag & Bauer 2013). The finer breakdown of task domains is a model assumption.

### 4.3 Groups as entities and as prior

Groups are nodes of their own. Membership is an edge type of its own and separate from trust. Group membership sets the base rate a and a small prior strength W of a new edge. The effect is supported: people cooperate more with the in-group, d ≈ 0.32 across 212 studies (Balliet, Wu & De Dreu 2014). The prior loses weight with every individual observation (Kunda & Thagard 1996).

Group knowledge often predicts aggregates usefully but individuals weakly, because the variance within groups is large (Jussim 2012). **A group-based prior must therefore never by itself justify or deny a permission.** This leaves unaffected the fact that groups act strongly on their members' uptake of evidence and verification behavior (long version, Chapter 7; Paper 2 (Rumpf, in preparation)); only the prediction of individual trustworthiness from membership is weak.

### 4.4 Groups as carriers of shared convictions

Groups develop norms and narratives, such as “Our information sources are more credible than others”. These act on the base rates of their members. Individual and group-related convictions remain separate: a person can belong to a group without sharing its convictions. Formally, anchoring to group convictions can be represented with the Friedkin-Johnsen model (Friedkin & Johnsen 1990). *It remains open under which conditions groups reinforce or change individual beliefs.*

## 5. Dynamic trust development

### 5.1 Evidence model instead of scalar

Each edge maintains, per context and dimension, two evidence accounts: r for positive, s for negative evidence. Added to these are the base rate a and the prior strength W. The opinion follows from them:

```math
b = \frac{r}{r+s+W}, \qquad d = \frac{s}{r+s+W}, \qquad u = \frac{W}{r+s+W}, \qquad E = b + a\,u
```

E is the expected trustworthiness. u is evidential certainty read inversely: much evidence yields a small u. The model corresponds to the Beta Reputation System (Jøsang & Ismail 2002). The advantage over a single trust value: **E = 0.5 without any observation (u = 1) is distinguishable from E = 0.5 after a thousand mixed observations (u close to 0).**

### 5.2 Initial trust

A new edge starts with r = s = 0, i.e. u = 1 and E = a. The base rate a arises from three sources:

```math
a_{A\to B,c} = w_1\,U_A + w_2\,P_{A,c} + w_3\,G_{A,B,c}, \qquad w_1+w_2+w_3 = 1
```

U is A's general propensity to trust, P the context-specific expectation, G the group or category prior. The prior strength W determines how much evidence is needed to override a. Beliefs act on a and W (Section 6.3).

Initial trust also arises from recommendations, proofs of identity and competence, known channels, limited collaboration and binding rules. Platforms and institutions act as gatekeepers. **A platform guarantee is itself only a source of evidence with its own uncertainty and no substitute for independent evidence.**

### 5.3 Updating and temporal decay

An event e at time interval Δt updates both accounts:

```math
r \leftarrow \lambda^{\Delta t}\,r + g^{+}, \qquad s \leftarrow \lambda^{\Delta t}\,s + g^{-}
```

```math
g^{\pm} = \varrho_e \cdot q_e \cdot w^{\pm}_{k} \cdot r_{e,c} \cdot \max(\pm v_e,\,0)
```

| Quantity | Meaning | Range |
| --- | --- | --- |
| λ | forgetting factor per unit of time | (0, 1] |
| ϱ | independence weight of the source | [0, 1] |
| q | diagnosticity: How costly would the signal be for a deceiver? | [0, 1] |
| w± | dimension weight for positive or negative evidence | > 0 |
| r(e,c) | relevance of the event for context c | [0, 1] |
| v | valence of the event | [−1, 1] |

Without forgetting (λ = 1), the result is independent of the order of events. With λ < 1, recent events deliberately count more. Without new evidence, r and s shrink. The uncertainty u rises toward 1, and E returns to the base rate a. **Trust therefore does not decay to zero, but to ignorance.** The half-life of evidence is:

```math
t_{1/2} = \frac{\ln 2}{-\ln \lambda}
```

At a constant evidence rate g per unit of time, the account saturates at g / (1 − λ). Complete certainty is therefore unattainable:

```math
u_{\min} = \frac{W}{W + \dfrac{g}{1-\lambda}}
```

![Without new evidence, trust returns to the base rate and uncertainty rises](../../docs/figures/fig-03-temporal-decay.png)

*Figure 3: Temporal decay according to Section 5.3 · illustrative parameters, 60 days*

Expected trust does not fall to zero but approaches the base rate. What is lost is the certainty of the assessment.

### 5.4 Conditional asymmetry

The effect of a single event of strength g on E, given a prior amount of evidence n = r + s + W, is:

```math
\Delta E^{+} = (1-E)\,\frac{g}{n+g}, \qquad \Delta E^{-} = -E\,\frac{g}{n+g}
```

This corresponds to the Bush-Mosteller and Rescorla-Wagner learning rule with a learning rate g / (n + g) that decreases as evidence grows. The classic rule with a constant learning rate is a special case. Three consequences follow:

- **Buffering.** A misstep weighs less after a long positive history. This is consistent with findings that existing trust cushions negative events (Cvetkovich et al. 2002; White et al. 2003).
- **Structural asymmetry.** At high E, the possible loss is larger than the possible gain, even with equal weights.
- **Dimension dependence.** The weights w+ and w− depend on the dimension.

| Event type | Ratio of w− to w+ | Evidence |
| --- | --- | --- |
| Integrity violation with deception | clearly greater than 1 | Schweitzer, Hershey & Bradlow 2006 |
| Integrity violation without deception | greater than 1 | Skowronski & Carlston 1989 |
| Competence error | less than or equal to 1 | Reeder & Brewer 1979; Kim et al. 2004 |
| Unreliability | close to 1, repairable | Schweitzer et al. 2006 |

A fixed assumption that negative experiences always act more strongly than positive ones is therefore unnecessary. **The asymmetry principle (Slovic 1993; Baumeister et al. 2001) holds as a tendency for integrity, not in general.**

### 5.5 Context transfer

An event acts on several contexts via r(e,c). An unrepaid loan strongly affects the context of lending money, partly integrity in general, and hardly professional competence. Model assumption: **integrity evidence transfers broadly across contexts, competence evidence narrowly.** An event must not be counted several times as independent evidence via domain and tags.

### 5.6 Propagation in the graph

Trust information propagates via third parties. The effect is supported and stronger for distrust (Burt & Knez 1995; Sommerfeld et al. 2007). Normatively, however, trust is not transitive (Christianson & Harbison 1997). The model separates functional trust (B can do the task) from referral trust (C judges others well). A recommendation by C about B is discounted by A's referral trust in C:

```math
b_{A:B} = b_{A\to C}\,b_{C\to B}, \quad d_{A:B} = b_{A\to C}\,d_{C\to B}, \quad u_{A:B} = d_{A\to C} + u_{A\to C} + b_{A\to C}\,u_{C\to B}
```

This is the discounting operator of Subjective Logic. **Along a chain, trust can only decrease and uncertainty can only increase.** Own experience, another's statement and independently verified information remain separate kinds of evidence. Descriptively, the least discounting occurs when C belongs to the in-group (H4a, Section 9.2).

### 5.7 Repetition, familiarity and source dependence

Repeated statements are more likely to be considered true, even without new evidence (Illusory Truth Effect; Hasher et al. 1977). The effect is small and robust: g = 0.37 after correction for publication bias across 182 studies (Ye et al. 2026). It grows logarithmically with the number of repetitions (Hassan & Barber 2021). The model therefore maintains two parallel accounts.

**Normative account.** n repetitions from sources with dependence D count only as an effective sample:

```math
n_{\text{eff}} = \frac{n}{1 + (n-1)\,D}, \qquad \lim_{n\to\infty} n_{\text{eff}} = \frac{1}{D}
```

At D = 1 (one original source), n_eff = 1, no matter how often the statement appears. At D = 0.5, any number of repetitions reaches at most the value of two independent sources.

![At D = 0.5, any number of repetitions counts at most as two sources](../../docs/figures/fig-04-source-dependence.png)

*Figure 4: Effective sample according to Section 5.7 · four degrees of dependence, 1 to 10 repetitions*

Only with independent sources does evidence grow with each repetition. Even at low dependence, the curve flattens early.

**Descriptive account.** It additionally contains a familiarity term:

```math
r^{\text{desc}} = r^{\text{norm}} + \varphi\,(1-m)\,\ln(1+R)
```

R is the number of perceived repetitions, φ the individual susceptibility, m the degree of accuracy focus. An accuracy focus at first contact dampens the effect (Brashier, Eliseev & Marsh 2020). Very frequent repetition can lower credibility again (Koch & Zerback 2013). The term therefore needs saturation.

**People distinguish genuine from apparent consensus poorly** (Yousif, Aboody & Keil 2019) and neglect correlated sources (Enke & Zimmermann 2019). Repetition also increases the credibility of the source itself (Mattavelli, Brambilla & Unkelbach 2025). This finding is preregistered; an independent replication has yet to be carried out.

### 5.8 The calibration gap

The difference between the two accounts is the central derived quantity:

```math
\Gamma_{A\to B,c} = E^{\text{desc}} - E^{\text{norm}}
```

Γ > 0 means unjustified trust (False Trust), Γ < 0 unjustified distrust (False Distrust). **Γ is the attack surface for social engineering and at the same time the target quantity for training.** The goal is calibrated trust, neither maximum trust nor maximum distrust; training is meant to reduce Γ in both directions (Paper 2 (Rumpf, in preparation)).

## 6. Psychological factors

People do not begin relationships without prior experience. The model assigns the factors to four levels, each with its own time scale, so that the same mechanism is not modeled twice.

| Level | Model variable | Change | Acts on |
| --- | --- | --- | --- |
| Disposition | propensity to trust U | very slow | base rate a |
| Beliefs | beliefs, context prior P | slow | a, W, valence v |
| Learning parameters | λ, w+, w−, prior strength W | medium | updating |
| Momentary state | activation H | fast | willingness to act, verification effort |

### 6.1 Disposition instead of basic trust

Instead of the term basic trust, the model uses the measurable propensity to trust. **It predicts trust independently, above all when little information about the counterpart is available** (Colquitt, Scott & LePine 2007). The propensity is partly dispositional. Twin studies estimate the heritability of trust behavior at about 10 to 20 percent (Cesarini et al. 2008). Other work finds hardly any genetic influence (Van Lange, Vinkhuyzen & Posthuma 2014). Uslaner (2002) regards generalized trust as largely resistant to experience.

### 6.2 Formative experiences and learning parameters

**According to the model, formative experiences change the disposition less than the context-specific priors and the learning parameters.** Evidence for experience-dependent priors comes from Alesina & La Ferrara (2002) and Dohmen et al. (2012). By contrast, Bauer (2015) finds no consistent effect of victimization on generalized trust in panel data. Resilience is the most common trajectory after stressful events (Bonanno 2004).

The activation H is read as an estimate of environmental volatility. In an environment experienced as unpredictable, a higher learning rate is appropriate (Behrens et al. 2007). In the model this means a smaller λ and a smaller W. Deviating volatility estimation has been described in anxiety (Browning et al. 2015). H is not a clinical trauma score and must not be used for diagnosis. Traumatic experiences do not lead to the same reactions in all people.

### 6.3 Beliefs

Beliefs are relatively stable convictions of an entity about itself, others or the world. They are properties of the evaluating node:

```math
\mathcal{B}_A = \{b_1,\ldots,b_n\}, \qquad b_i = (p_i,\; q_i,\; C_i)
```

p is the content, q the strength in [0,1], C the set of affected contexts. Beliefs act at three points.

| Effect | Model variable | Example |
| --- | --- | --- |
| Advance trust | base rate a | “People are basically honest” raises a |
| Persistence | prior strength W | “I am good at judging people” raises W: evidence has a weaker effect |
| Interpretation | valence v and weights w± | “Once a liar, always a liar” raises w− for integrity |

The interpretation function is:

```math
v_{A,e,c} = f(e,\,c,\,\mathcal{B}_A) \in [-1,\,1]
```

Example: A colleague publicly contradicts a manager. Someone who reads contradiction as integrity evaluates it positively. Someone who understands loyalty as silence evaluates it negatively.

**Opposite-direction updating, however, is the exception.** Across 52 topics, Wood & Porter (2019) found hardly any backfire effects. Groups mostly update in parallel in the same direction (Coppock 2022). The model expects sign reversals only for ambiguous events. For unambiguous events, people differ in a, W and strength, not in direction. Measurable candidates for beliefs are Primal World Beliefs (Clifton et al. 2019), implicit theories about changeability (Haselhuhn, Schweitzer & Wood 2010) and the Hostile Attribution Bias (Crick & Dodge 1994).

### 6.4 Feedback loop and learning trap

Beliefs, interpretation and experience form a cycle: belief, interpretation, change in trust, behavior, new experience, confirmation or revision. The cycle is asymmetric. **Someone who does not trust does not interact and receives no corrective evidence** (Denrell 2005). People therefore underestimate the trustworthiness of others, and symmetric feedback reduces this cynicism (Fetchenhauer & Dunning 2010). Expectations can also be self-fulfilling (Kelley & Stahelski 1970).

In the model this means: if E falls below the threshold for interaction, no more evidence arrives. Only the temporal decay λ then returns the edge to the base rate.

![Distrust stabilizes itself: without interaction no evidence arises](../../docs/figures/fig-05-learning-trap.png)

*Figure 5: Feedback loop according to Section 6.4 · learning loop and learning trap*

Above the threshold the loop runs and corrects itself. Below it, it ends in a dead end: the judgment persists because nothing can contradict it any longer. The learning trap has a collective form: a group that discredits outside sources in advance receives, as a whole, no corrective evidence (long version, Section 7.8).

Whether experiences change generalized trust is contested. In the laboratory it shifts in the direction of the experience (Paxton & Glanville 2015). In panel data, some experiences have an effect, for example unemployment (Mewes et al. 2021).

### 6.5 Momentary state

**Stress and time pressure do not change the evaluation E, but the willingness to act and the verification effort.** A person can trust another in principle and still not feel sure enough in a particular situation. Trust evaluation and willingness to act remain separate variables.

## 7. Decision layer and model architecture

### 7.1 Three separate questions

A trust decision breaks down into three checks that do not substitute for one another:

| Question | Checks | Model variable |
| --- | --- | --- |
| Identity | Who is the entity? | evidence on edge attribution |
| Authorization | May it trigger this action? | permission P |
| Factual correctness | Is the specific statement or request correct? | evidence on the event itself |

**A confirmed identity proves neither permission nor correctness.** Trust in the person proves none of the three.

### 7.2 Threshold rule for permissions

An action x yields the benefit N for a legitimate request and the loss L in case of abuse. It is only worthwhile if the probability of legitimacy exceeds the threshold θ:

```math
\theta_x = \frac{L_x}{L_x + N_x}
```

The permission is granted if the normative trust minus an uncertainty penalty reaches the threshold:

```math
E^{\text{norm}} - \kappa\,u \;\ge\; \theta_x
```

κ is the risk aversion. Two consequences follow. **The threshold depends only on the action, not on the person.** And high uncertainty lowers the permission even when the expected value is high. Example: A bank transfer with L = EUR 50,000 and N = EUR 500 yields θ ≈ 0.99. No realistically attainable personal trust suffices on its own. The action needs additional independent evidence.

### 7.3 Verification rule

An additional verification with cost K and detection probability τ is worthwhile if:

```math
K \;<\; \tau \cdot (1 - E^{\text{norm}}) \cdot L_x
```

**Verifications must therefore be cheap so that they are still triggered when residual doubt is small.** This justifies the requirement for low-effort procedures in training. In organizations, K and τ are not set individually but by norm, role and the presumed verification by others; this is treated in Paper 2 (Rumpf, in preparation).

### 7.4 Overview of model variables

| Variable | Symbol | Function |
| --- | --- | --- |
| Trust, distrust, uncertainty | b, d, u | opinion per edge, context, dimension |
| Expected trustworthiness | E | b + a·u |
| Evidence accounts | r, s | positive and negative evidence |
| Base rate and prior strength | a, W | advance trust and persistence |
| Forgetting factor | λ | temporal decay of evidence |
| Source dependence | D | correlation of sources |
| Diagnosticity | q | cost of faking a signal |
| Repetition | R | perceived frequency |
| Calibration gap | Γ | descriptive minus normative |
| Vulnerability | L | loss in case of abuse |
| Permission | P | granted scope of action |
| Beliefs | B | filter for a, W, v |
| Activation | H | momentary state |

The long version adds a mapping strength μ between dimensions and security objectives and two derived group-level quantities, verification coverage C and the assumed detection rate τ_I (long version, Section 6.4). They are not needed here.

### 7.5 Architecture and processing steps

The model consists of six layers: entities, relationships, experiences, beliefs, psychological state and decision. Each event passes through seven steps:

1. Record the event.
2. Determine context and dimension.
3. Evaluate the source: independence D and diagnosticity q.
4. Interpret: valence v, colored by beliefs in the descriptive account.
5. Update both evidence accounts, with temporal decay.
6. Adjust slow variables: priors and beliefs.
7. Decide: apply the threshold rule and the verification rule.

![The gap between felt and justified trust is the attack surface](../../docs/figures/fig-06-architecture.png)

*Figure 6: Processing of an event · two evidence accounts, one decision*

Each event feeds two accounts. **Decisions are made only on the basis of the normative account**; the difference from the descriptive account is the calibration gap Γ. The temporal decay λ acts on both accounts. This process description is an architectural hypothesis.

## 8. Trust from an attacker's perspective

### 8.1 Trust and vulnerability

Trust does not create a security gap. **A vulnerability arises when a positive expectation is combined with an exploitable scope of action.** The loss depends on the permission P and the size of the loss L, not on the level of trust. Data on internal fraud support this: owners and executives caused a median loss of USD 500,000, regular employees USD 60,000 (ACFE 2024). The data are correlational.

### 8.2 Abuse of trust and two classes of attack

Abuse of trust occurs when an actor deliberately uses a positive expectation to gain an advantage against the interests or agreed limits of the trusting entity. **A disappointed expectation does not prove hostile intent.** Errors, overload, misunderstandings and conflicts of interest also produce negative experiences. In the model, a competence error therefore counts differently from a deception (Section 5.4).

**Two classes of attack.** Abuse attacks exploit a scope of action P that has already been granted; their loss follows G1. Calibration attacks instead shift the evaluation itself: they enlarge the calibration gap Γ without touching any permission. Social engineering usually combines both stages: first calibrate, then abuse. The techniques in Section 8.4 act predominantly as calibration attacks; the abuse is the subsequent action. At the macro level, calibration attacks can cause harm even without an abuse stage, for example as a lasting miscalibration of a public. The companion paper [Case Study 1](../../docs/case-study-01-populist-techniques.md) applies the model to populist argumentation techniques as calibration attacks at the macro level.

### 8.3 Three levels of analysis

| Level | Guiding question |
| --- | --- |
| Motivation | What advantage does the actor want to gain? |
| Opportunity | Which relationship or permission opens up the possibility? |
| Approach | How can this relationship be abused? |

The levels correspond to the Fraud Triangle (Cressey 1953). The presumed motivation serves to form hypotheses, not to assign blame.

### 8.4 Attacks as operations on model variables

**Every social engineering technique can be read as an intervention in a specific model variable.** This makes visible which countermeasure acts at which point.

| Technique | Manipulated variable | Effect in the model | Countermeasure |
| --- | --- | --- | --- |
| Impersonation, deepfake voice | edge attribution | attacker inherits the evidence r of another node | verify identity via an independent channel |
| Authority or group signal | base rate a | high advance trust without evidence | verify permission separately from status |
| Sock puppets, fake reviews | repetition R, hidden dependence D | descriptive account grows, normative does not | count independent origins |
| Long trust-building | account r via cheap events | high E from evidence with low diagnosticity q | weight evidence by stakes |
| Context switch | transfer r(e,c) | trust from a harmless domain is used for a risky one | keep contexts separate |
| Time pressure, secrecy | verification cost K, accuracy focus m | verification does not happen, familiarity has a stronger effect | make verification mandatory per action class |
| Appeal to beliefs | valence v | event is interpreted favorably | check questions on one's own interpretation |
| Blanket denial of genuine evidence | distrust d against true evidence | Liar's Dividend (Chesney & Citron 2019) | provenance records, fact-checking |
| Normalization (“Everyone here does it this way”) | descriptive norm, verification cost K | verification counts as unusual and does not happen | make verification visible as a team norm |
| Exploiting protection delegation | assumed detection rate τ_I | A assumes that what got through has been checked | make the institution's error rate visible |
| Compromised colleague account, insider | group prior G, discounting | in-group is hardly discounted, request counts as internal | verify the action class, not the sender group |
| Manipulated reputation scores | the model itself | false evidence in the normative account | log evidence provenance |

The rows on normalization, protection delegation and compromised colleague accounts concern the group level; their quantities and rules are developed in Paper 2 (Rumpf, in preparation). The techniques occur in combination. Example: a fraudulent identity is visible on several platforms for months, collects seemingly independent recommendations and then makes a payment request under time pressure. R is high, D close to 1, q low, K artificially raised.

## 9. Core assumptions and hypotheses

After the literature review, the long version considers four statements as established and treats them as core assumptions. Three of them concern the model presented here; G4 concerns groups and is treated in Paper 2 (Rumpf, in preparation). The hypotheses below are the ones that concern the model itself.

### 9.1 Core assumptions

| ID | Core assumption | Reference in the model | Key evidence |
| --- | --- | --- | --- |
| G1 | The loss from an abuse of trust depends on the scope of action granted and the vulnerability, not on the level of trust. | Sections 7.2 and 8.1 | Mayer et al. 1995; Saltzer & Schroeder 1975; ACFE 2024 |
| G2 | Trust information propagates through social relationships, distrust more strongly than trust. | Section 5.6 | Burt & Knez 1995; Sommerfeld et al. 2007 |
| G3 | Repetition increases the perceived truth of statements without new evidence. | Section 5.7 | Hasher et al. 1977; Ye et al. 2026 |

### 9.2 Hypotheses on the model

**H1 – Diagnosticity and provenance evidence.** If the cost of producing a convincing result falls, features of the result lose their informative value for trustworthiness. Provenance and process evidence gain weight only if they are expensive for deceivers and understandable for recipients. Blanket AI labeling also lowers the credibility of true content.

**H2 – Groups as a weak prior.** Group membership determines the base rate of a new trust edge. Its influence decreases with each individual observation and predicts the behavior of individuals only weakly. This concerns the assessment; on evidence intake and verification behavior, groups have a strong effect (long version, G4 and Chapter 7).

**H4 – Discounted propagation.** Along a referral chain, justified trust decreases and uncertainty grows. People discount referrals less strongly than the dependence of the sources requires.

- **H4a – In-group.** Discounting is lowest when the referrer belongs to the in-group. Compromised colleague accounts and internal forwards are therefore hardly verified.

**H5 – Experience acts on priors and learning parameters.** Formative experiences change context-specific priors and learning parameters more strongly than the generalized propensity to trust. Environments experienced as unpredictable increase the learning rate.

**H5a – Conditional asymmetry.** Negative evidence weighs more heavily than positive evidence in integrity violations, especially with deception. This does not apply to competence errors. Extensive positive prior evidence buffers individual negative events.

**H9 – Transfer of familiarity to entities.** Repeated encounters with a source, organization or agent increase its subjective trust rating without new independent evidence. The effect grows with diminishing returns as frequency increases, decreases with accuracy focus and reverses with oversaturation.

**H10 – Beliefs as prior and interpretive filter.** Beliefs determine base rate and prior strength and color the interpretation of ambiguous events. With unambiguous events, people with different beliefs update in the same direction, but to different degrees.

**H11 – Asymmetric feedback loop.** Distrust stabilizes itself because it prevents corrective experiences. Trust is corrected more easily because disappointments are observed. Edges change faster than context priors, these faster than beliefs. The feedback loop also applies collectively: Groups that discredit outside sources stabilize their distrust as a whole (long version, Section 7.8).

### 9.3 Evidence status

| ID | Status | Supporting sources | Limiting sources |
| --- | --- | --- | --- |
| H1 | partly supported | Chesney & Citron 2019; Schiff et al. 2025; Nightingale & Farid 2022; Spence 1973 | Altay & Gilardi 2024; Wang et al. 2026; lack of user studies on Content Credentials |
| H2 | well supported | Balliet et al. 2014; Foddy et al. 2009; Kunda & Thagard 1996 | Jussim 2012 |
| H4 | normatively grounded, descriptively partly supported | Jøsang 2016; Enke & Zimmermann 2019 | Christianson & Harbison 1997 |
| H5 | partly supported | Dohmen et al. 2012; Behrens et al. 2007; Reimann et al. 2017 | Cesarini et al. 2008; Uslaner 2002; Bauer 2015 |
| H5a | partly supported | Kim et al. 2004; Schweitzer et al. 2006; Skowronski & Carlston 1989 | Gal & Rucker 2018 |
| H9 | first preregistered evidence | Mattavelli et al. 2025; Montoya et al. 2017 | Brashier et al. 2020; Koch & Zerback 2013 |
| H10 | partly supported | Lord, Ross & Lepper 1979; Delgado et al. 2005; Haselhuhn et al. 2010 | Wood & Porter 2019; Coppock 2022 |
| H11 | partly supported | Denrell 2005; Fetchenhauer & Dunning 2010; Paxton & Glanville 2015 | Uslaner 2002; Bauer 2015; Mewes et al. 2021 |

### 9.4 Operationalization

For each hypothesis, the following must be specified before testing: independent and dependent variables, confounders, measurement methods, expected direction and criteria for confirmation or refutation. The psychological hypotheses (H2, H5, H9 to H11) need designs of their own, distinct from those for effectiveness hypotheses.

## 10. What the model predicts

**Testable statements on distrust, contexts, course over time and global events follow from the evidence model.** All statements in this section are derivations from the equations in Sections 5 and 7. They are predictions, not findings. Where the literature already fits, this is noted.

### 10.1 Trust and distrust

| No. | Prediction | Derivation | Testable by |
| --- | --- | --- | --- |
| V1 | Young relationships react strongly to individual events, old ones hardly at all. | learning rate g / (n + g) decreases with amount of evidence | trust game with varied history |
| V2 | Ambivalent relationships are stable, unknown ones volatile, although both have E close to 0.5. | same E, different u | separate scales for trust and distrust |
| V3 | A misstep costs more in absolute terms at high trust than at medium trust. | ΔE− is proportional to E | consistent with the asymmetry principle (Slovic 1993) |
| V4 | Distrust recovers more slowly than trust falls, even with equal weights. | below the interaction threshold no evidence arrives; only temporal decay acts | symmetric vs. asymmetric feedback (Fetchenhauer & Dunning 2010) |
| V5 | Many small positive experiences produce subjectively high trust that normatively does not support risky actions. | descriptively every event counts, normatively q weights evidence by stakes | simulation of long trust building |

V5 describes the pattern of investment fraud and romance scams: a long phase of cheap confirmations, then a request with high loss.

### 10.2 Contexts

| No. | Prediction | Derivation | Testable by |
| --- | --- | --- | --- |
| V6 | A discovered deception lowers trust in all contexts, a competence error only in its domain. | integrity evidence transfers broadly, competence evidence narrowly | vignette study with context variation |
| V7 | Attacks succeed preferentially in contexts with little evidence but a familiar relationship. | u is context-specific, familiarity is not | analysis of real incidents by context switch |
| V8 | Group and status signals dominate first contacts and lose influence with evidence. | influence of the base rate on E is a·u | supported for categories (Kunda & Thagard 1996) |
| V9 | In one-off contacts, for example on platforms, category and platform signals remain permanently decisive. | u stays close to 1 because individual evidence never arises | field experiments on marketplaces |

### 10.3 Loss over time

| No. | Prediction | Derivation | Testable by |
| --- | --- | --- | --- |
| V10 | Without contact, trust does not fall to zero but returns to the base rate. | r and s shrink, E tends towards a | longitudinal study of dormant relationships |
| V11 | After a long break, a relationship feels intact but does not support risky actions. | E close to a with a high base rate, but u high | comparison of assessment and willingness to act |
| V12 | Infrequent contact permanently limits the achievable certainty. | u_min depends on the evidence rate g | simulation with varied contact frequency |
| V13 | A breach fades with the half-life of the evidence, provided nothing recalls it. | s decays with λ | reminder cues as an experimental condition |
| V14 | Competence evidence ages faster than integrity evidence in rapidly changing domains. | additional assumption: λ is dimension-dependent | open; to be tested as an assumption |

### 10.4 News and global effects

A news item about a category, for example banks, authorities, strangers online or AI content, shifts the base rate a of that category. The effect on an individual edge is:

```math
\Delta E = u \cdot \Delta a
```

**Global events therefore hit edges with little evidence fully and well-evidenced edges hardly at all.**

![A global shock hits weakly evidenced relationships twenty times more strongly](../../docs/figures/fig-09-global-shock.png)

*Figure 7: Effect of a base rate shift according to Section 10.4 · five example edges, illustrative values*

The same news item has effects of different strength depending on the evidential situation. Well-evidenced relationships remain almost unaffected.

| No. | Prediction | Derivation | Testable by |
| --- | --- | --- | --- |
| V15 | Scandals and waves of fraud lower trust in strangers and institutions more than in acquaintances. | ΔE = u·Δa | panel data before and after events |
| V16 | After shocks, people withdraw to known relationships. | only edges with small u remain above the threshold | change in the radius of trust (Delhey et al. 2011) |
| V17 | Intensive reporting on a single event decouples perceived from actual risk. | the descriptive account grows with ln(1 + R); normatively, n_eff stays 1 | media intensity against event frequency |
| V18 | Public distrust persists as long as reporting continues and then decays with the half-life. | repetition offsets temporal decay | time series after the end of reporting |
| V19 | If the base rate for the authenticity of content falls, everyone accumulates evidence more slowly, and verified channels gain value. | q decreases for content evidence; u remains high throughout the graph | use of verified channels over time |
| V20 | Groups with shared, mutually dependent sources overestimate their certainty. | high dependence D is read as independence | source overlap against confidence of judgment |
| V21 | At network level, trust recovers more slowly after a shock than it fell. | distrust propagates more strongly (G2) and stabilizes itself (H11) | agent-based simulation, comparison with survey series |

V15 and V19 fit existing findings: Blanket AI labeling also lowers the credibility of true headlines (Altay & Gilardi 2024), and pointing to possible forgery benefits the accused (Schiff et al. 2025). Predictions on groups and organizations (V22 to V27) are treated in Paper 2 (Rumpf, in preparation).

### 10.5 Limits of the predictions

The predictions are qualitative. Quantitative statements need estimated parameters λ, W, w± and φ per population and context. The formula ΔE = u·Δa assumes that news items only shift the base rate. If a news item concerns a specific entity, it is evidence on that entity's edge.

## 11. Research plan and open questions

### 11.1 Phases

The first three phases of the research plan concern the model itself:

| Phase | Goal | Result |
| --- | --- | --- |
| 1 Concepts and literature | cross-check marked references; establish the link to Rousseau, Mayer, Lewicki, Jøsang, Lee & See | consistent conceptual model with supported and hypothetical assumptions kept separate |
| 2 Formal specification | fully define the evidence model, context transfer, discounting and both accounts | mathematically consistent specification |
| 3 Minimal simulation | small graph with normative and descriptive account | visible calibration gap Γ per scenario |

Phases 4 and 5 (training, agent prototype) belong to the applications; phase 6 (preregistered evaluation) tests the hypotheses, including those of this paper (long version, Section 15.1). The technical verification of a simulation is not an empirical validation of the psychological model.

### 11.2 Simulation scenarios

1. Building a new professional relationship.
2. A single serious breach after a short and after a long history (V1, V3).
3. Deception versus competence error at equal event strength (H5a, V6).
4. Long trust-building with cheap events, then a high-risk request (V5).
5. A hundred repetitions of a claim at D = 1, 0.5 and 0 (V17).
6. A dormant relationship over several half-lives (V10 to V12).
7. Global news with a shift in the base rate (V15, V16).
8. Distrust below the interaction threshold with and without enforced feedback (V4).
9. Referral chain with three links (H4).

### 11.3 Open questions

**Theoretical**

- Are trust and distrust two dimensions or two readings of the same evidence?
- How do trust, credibility and reputation differ in the model?
- What role do emotion and intuition play beyond activation H?
- Does the model need a quantity of its own for normative expectations in order to distinguish trust from mere reliance (Chen 2021)?

**Mathematical**

- How are D and q estimated in everyday life?
- Does the forgetting factor differ by dimension and context (V14)?
- What form does the saturation of the familiarity term take?
- How is context transfer r(e,c) parameterized without counting evidence twice?
- How do beliefs change formally: as a slow prior over priors?

## 12. Limitations

- **Quantification.** Even a triple of b, d and u is an abstraction. It has not been shown that human trust can be represented this completely.
- **Subjectivity.** The model must separate observable facts from subjective assessments.
- **Causality.** An observed change in trust does not show which factor caused it.
- **Abundance of parameters.** λ, W, w±, φ, D and q are numerous. Without hierarchical estimation and model comparison, the model risks becoming unfalsifiable.
- **Identifiability.** Base rate and prior strength can be separated from behavior only with suitable designs.
- **Normative standard.** The normative account presupposes that D and q can be determined. In everyday life they can often only be estimated.
- **Psychological simplification.** Disposition, formative experiences, trauma and beliefs are complex concepts. Individual parameters are deliberate simplifications.
- **Manipulation of the model.** A system that computes trust itself becomes a target of attack (Section 8.4).
- **Trust or reliance.** The model does not represent normative expectations separately. In Chen's (2021) distinction, it mainly describes calibrated reliance (Section 3.5).

## 13. Ethics and law

The model serves self-reflection, training, simulation and the assessment of technical systems. **It does not serve the assessment of persons for decisions by third parties.**

- **EU AI Act, Art. 5(1)(c).** Prohibited are AI systems that evaluate persons over a period of time based on their social behavior or personal characteristics, where this leads to detrimental treatment in unrelated contexts or to disproportionate detrimental treatment. A graph that transfers group trust and carries it forward across contexts would come close to this prohibited practice.
- **GDPR Art. 22.** According to CJEU judgment C-634/21 (SCHUFA, 7 December 2023), the very creation of a score can be an automated decision.
- **GDPR Art. 9.** Recorded beliefs can be data on philosophical beliefs or health.
- **Discrimination.** Group priors can confirm themselves. They must never carry a decision on their own (Section 4.3).

The legal classification is an initial assessment and does not replace a legal review.

## 14. Conclusion

Artificially generated content devalues the features from which people have so far read trustworthiness. The appropriate response is neither blind trust nor blanket distrust.

**The model describes trust as an evidential situation with three components: trust, distrust and ignorance.** It separates the subjective assessment from the evidence-based one and makes their difference, the calibration gap Γ, measurable. Attacks, training and technical controls can be described as interventions in the same quantities. The predictions derived here are untested, and the hypotheses keep their stated evidence status.

Trust is engineered: not because human trust could be reduced to an algorithm, but because decisions that rest on trust can be structured, verified and improved. The result is not a machine that determines whom we should trust. It is a model that explains why we trust, when we are wrong and which action is justifiable under uncertainty.

## References

- Rumpf, J. (2026). Trust is Engineered. Working paper, version 0.6 (draft). https://github.com/JoeRu/trust-is-engineered
- ACFE (2024). Occupational Fraud 2024: A Report to the Nations.
- Alesina, A. & La Ferrara, E. (2002). Journal of Public Economics, 85(2), 207–234.
- Altay, S. & Gilardi, F. (2024). PNAS Nexus, 3(10), pgae403.
- Balliet, D., Wu, J. & De Dreu, C. K. W. (2014). Psychological Bulletin, 140(6), 1556–1581.
- Bauer, P. C. (2015). European Sociological Review, 31(4), 397–417.
- Baumeister, R. F., Bratslavsky, E., Finkenauer, C. & Vohs, K. D. (2001). Review of General Psychology, 5(4), 323–370.
- Behrens, T. E. J. et al. (2007). Nature Neuroscience, 10(9), 1214–1221.
- Bonanno, G. A. (2004). American Psychologist, 59(1), 20–28.
- Brashier, N. M., Eliseev, E. D. & Marsh, E. J. (2020). Cognition, 194, 104054.
- Browning, M. et al. (2015). Nature Neuroscience, 18(4), 590–596.
- Burt, R. S. & Knez, M. (1995). Rationality and Society, 7(3), 255–292.
- Cesarini, D. et al. (2008). PNAS, 105(10), 3721–3726.
- Chen, M. (2021). Trust and Trust-Engineering in Artificial Intelligence Research: Theory and Praxis. Philosophy & Technology, 34, 1429–1447. https://doi.org/10.1007/s13347-021-00465-4 (checked against full text)
- Chesney, R. & Citron, D. (2019). Deep Fakes: A Looming Challenge. California Law Review, 107, 1753–1820.
- Christianson, B. & Harbison, W. S. (1997). Why isn't trust transitive? Security Protocols Workshop, LNCS 1189, 171–176.
- CJEU, judgment of 7 December 2023, C-634/21 (SCHUFA).
- Clifton, J. D. W. et al. (2019). Primal world beliefs. Psychological Assessment, 31(1), 82–101.
- Colquitt, J. A., Scott, B. A. & LePine, J. A. (2007). Journal of Applied Psychology, 92(4), 909–927.
- Coppock, A. (2022). Persuasion in Parallel. University of Chicago Press.
- Cressey, D. R. (1953). Other People's Money. Free Press.
- Crick, N. R. & Dodge, K. A. (1994). Psychological Bulletin, 115(1), 74–101.
- Cvetkovich, G. et al. (2002). Risk Analysis, 22(2), 359–367.
- Delgado, M. R., Frank, R. H. & Phelps, E. A. (2005). Nature Neuroscience, 8(11), 1611–1618.
- Delhey, J., Newton, K. & Welzel, C. (2011). American Sociological Review, 76(5), 786–807.
- Denrell, J. (2005). Psychological Review, 112(4), 951–978.
- Dohmen, T., Falk, A., Huffman, D. & Sunde, U. (2012). Review of Economic Studies, 79(2), 645–677.
- Enke, B. & Zimmermann, F. (2019). Review of Economic Studies, 86(1), 313–332.
- Fetchenhauer, D. & Dunning, D. (2010). Why so cynical? Psychological Science, 21(2), 189–193.
- Foddy, M., Platow, M. J. & Yamagishi, T. (2009). Psychological Science, 20(4), 419–422.
- Freitag, M. & Bauer, P. C. (2013). Public Opinion Quarterly, 77, 24–44.
- Friedkin, N. E. & Johnsen, E. C. (1990). Journal of Mathematical Sociology, 15(3–4), 193–206.
- Gal, D. & Rucker, D. D. (2018). Journal of Consumer Psychology, 28(3), 497–516.
- Hardin, R. (2002). Trust and Trustworthiness. Russell Sage Foundation.
- Haselhuhn, M. P., Schweitzer, M. E. & Wood, A. M. (2010). Psychological Science, 21(2), 181–183.
- Hasher, L., Goldstein, D. & Toppino, T. (1977). Frequency and the Conference of Referential Validity. Journal of Verbal Learning and Verbal Behavior, 16(1), 107–112.
- Hassan, A. & Barber, S. J. (2021). Cognitive Research: Principles and Implications, 6, 38.
- Jussim, L. (2012). Social Perception and Social Reality. Oxford University Press.
- Jøsang, A. & Ismail, R. (2002). The Beta Reputation System. 15th Bled eConference.
- Jøsang, A. (2016). Subjective Logic. Springer.
- Kelley, H. H. & Stahelski, A. J. (1970). Journal of Personality and Social Psychology, 16(1), 66–91.
- Kim, P. H., Ferrin, D. L., Cooper, C. D. & Dirks, K. T. (2004). Journal of Applied Psychology, 89(1), 104–118.
- Koch, T. & Zerback, T. (2013). Journal of Communication, 63(6), 993–1010.
- Kunda, Z. & Thagard, P. (1996). Psychological Review, 103(2), 284–308.
- Lee, J. D. & See, K. A. (2004). Human Factors, 46(1), 50–80.
- Lewicki, R. J. & Bunker, B. B. (1996). In Kramer & Tyler (Eds.), Trust in Organizations. Sage. (to be checked)
- Lewicki, R. J., McAllister, D. J. & Bies, R. J. (1998). Academy of Management Review, 23(3), 438–458.
- Lord, C. G., Ross, L. & Lepper, M. R. (1979). Journal of Personality and Social Psychology, 37(11), 2098–2109.
- Mattavelli, S., Brambilla, M. & Unkelbach, C. (2025). Repeating statements increases source credibility. Personality and Social Psychology Bulletin, 52(9), 2724–2737.
- Mayer, R. C., Davis, J. H. & Schoorman, F. D. (1995). An Integrative Model of Organizational Trust. Academy of Management Review, 20(3), 709–734.
- McKnight, D. H., Choudhury, V. & Kacmar, C. (2002). Information Systems Research, 13(3), 334–359.
- McKnight, D. H., Cummings, L. L. & Chervany, N. L. (1998). Academy of Management Review, 23(3), 473–490.
- Mewes, J., Fairbrother, M., Giordano, G. N., Wu, C. & Wilkes, R. (2021). Social Science Research, 95, 102537.
- Montoya, R. M. et al. (2017). Psychological Bulletin, 143(5), 459–498.
- Nightingale, S. J. & Farid, H. (2022). PNAS, 119(8), e2120481119.
- O'Neill, O. (2002). A Question of Trust. Cambridge University Press.
- Paxton, P. & Glanville, J. L. (2015). Is trust rigid or malleable? Social Psychology Quarterly, 78(2), 194–204.
- Reeder, G. D. & Brewer, M. B. (1979). Psychological Review, 86(1), 61–79.
- Regulation (EU) 2016/679 (GDPR), Art. 9 and Art. 22.
- Regulation (EU) 2024/1689 (AI Act), Art. 5(1)(c); Art. 15 (accuracy, robustness and cybersecurity).
- Reimann, M., Schilke, O. & Cook, K. S. (2017). Trust is heritable, whereas distrust is not. PNAS, 114(27), 7007–7012.
- Rousseau, D. M., Sitkin, S. B., Burt, R. S. & Camerer, C. (1998). Not so different after all. Academy of Management Review, 23(3), 393–404.
- Saltzer, J. H. & Schroeder, M. D. (1975). Proceedings of the IEEE, 63(9), 1278–1308.
- Schiff, K. J., Schiff, D. S. & Bueno, N. S. (2025). The Liar's Dividend. American Political Science Review, 119(1), 71–90.
- Schweitzer, M. E., Hershey, J. C. & Bradlow, E. T. (2006). Promises and lies. Organizational Behavior and Human Decision Processes, 101(1), 1–19.
- Skowronski, J. J. & Carlston, D. E. (1989). Psychological Bulletin, 105(1), 131–142.
- Slovic, P. (1993). Perceived risk, trust, and democracy. Risk Analysis, 13(6), 675–682.
- Sommerfeld, R. D., Krambeck, H.-J., Semmann, D. & Milinski, M. (2007). PNAS, 104(44), 17435–17440.
- Spence, M. (1973). Job Market Signaling. Quarterly Journal of Economics, 87(3), 355–374.
- Uslaner, E. M. (2002). The Moral Foundations of Trust. Cambridge University Press.
- Van Lange, P. A. M., Vinkhuyzen, A. A. E. & Posthuma, D. (2014). PLoS ONE, 9(4), e93880.
- Wang, Sturgis & de Kadt (2026). AI labeling reduces the perceived accuracy of online content but has limited broader effects. Telematics and Informatics, 107. (to be checked)
- White, M. P. et al. (2003). Risk Analysis, 23(4), 717–726.
- Wood, T. & Porter, E. (2019). The elusive backfire effect. Political Behavior, 41(1), 135–163.
- Ye et al. (2026). Nature Communications, 17, 3270. (author list to be checked)
- Yousif, S. R., Aboody, R. & Keil, F. C. (2019). The illusion of consensus. Psychological Science, 30(8), 1195–1204.
