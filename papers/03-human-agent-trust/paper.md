# Engineering Calibrated Trust between Humans, Agents and Machines: Evidence Accounts, Decay and Re-verification

> **DRAFT.** Work in progress, not peer reviewed and not empirically validated. Derived from the working paper *Trust is Engineered* v0.6 ([long version](../../docs/trust-is-engineered.md)); identifiers and evidence status follow it.

Johannes Rumpf ([ORCID 0009-0001-8675-0608](https://orcid.org/0009-0001-8675-0608)) · Version 0.1 · 18 October 2026 · DOI [10.5281/zenodo.23813132](https://doi.org/10.5281/zenodo.23813132)

## Abstract

AI agents now read content, call tools and trigger actions on behalf of people and other machines. This raises a practical question: how can trust between human and agent, and between machines, be established and verified on a recurring basis? This paper applies a graph-based evidence model of trust to technical nodes. Each edge holds an opinion of trust, distrust and uncertainty, built from positive and negative evidence accounts with a forgetting factor. With machines, evidence, temporal decay and permission can be implemented explicitly instead of only described. We derive five elements. First, attestation and identity set only the base rate; a correctly identified agent starts with full uncertainty. Second, each model quantity maps to a technical mechanism, from signed requests to short-lived tokens and diverse verifiers. Third, the forgetting factor yields a latest re-verification interval per action class, so riskier permissions are re-verified more often. Fourth, three trust directions (human→agent, agent→human or content, machine→machine) have different core problems and risks. Fifth, we hypothesize (H15c) that for agents utility becomes a risk dimension of its own that cannot be mapped to availability or data integrity. The paper states the related hypotheses, one prediction and eight rules. All are derivations from the model and have not been empirically tested.

**Keywords:** human-agent trust; machine-machine trust; Subjective Logic; temporal decay; re-verification; Zero Trust; utility risk

Identifiers G (core assumption), H (hypothesis), V (prediction) and S (rule) follow the long version [Rumpf 2026a, v0.6] so that they stay stable across papers.

## 1. Introduction

### 1.1 Trust under generative AI

AI slop, deepfakes, love scams and AI-generated identities change the conditions under which people trust information and other entities. Content alone no longer determines credibility. What becomes relevant is where it comes from, how it was created and through which channel it arrives. One of the questions this raises is technical: may an AI agent that identifies itself correctly also trigger the requested action?

Generative AI lowers the cost of producing a convincing result. A signal is only credible if it is costly for deceivers (Spence 1973). Features of the result therefore lose informative value. Weight shifts to the traceable process of creation, verifiable evidence and the sources used (long version, Sections 1.1 and 1.2).

### 1.2 The problem

The working paper *Trust is Engineered* treats two application problems with one model (long version, Section 1.3). This paper addresses the second one:

**Problem B – Integrating machines.** How can trust between human and agent, and between machines, be established and verified on a recurring basis?

The first problem, training people to recognize abuse of trust, is treated in Paper 2 (Rumpf 2026c). Both problems have the same structure: an entity must decide which action it allows another entity under incomplete evidence. The corresponding research question of the long version asks which rules for agent systems and information security follow from the model.

### 1.3 Contribution

The same model applies to technical nodes. The difference is that with machines, evidence, temporal decay and permission can be implemented explicitly instead of only described. The paper contributes:

1. a procedure for establishing trust in a technical entity, in which attestation sets only the base rate (Section 6);
2. a mapping of model quantities to technical mechanisms (Section 7);
3. a re-verification interval derived from temporal decay (Section 8);
4. an analysis of the three trust directions human→agent, agent→human or content, and machine→machine (Sections 5 and 9);
5. utility as a separate risk dimension for agents (Section 10).

Section 11 states the hypotheses, Section 12 the prediction and rules, Section 13 the research plan. The paper ends with limitations, ethics and law, and a conclusion. These parts are derivations from the model and have not yet been empirically tested.

## 2. Related work

The model represents trust as an opinion in Subjective Logic (Jøsang 2016) and updates it like the Beta Reputation System (Jøsang & Ismail 2002); it keeps the normative point that trust is not transitive (Christianson & Harbison 1997). For human trust in automation, it builds on the distinction of performance, process and purpose and on the findings on misuse and disuse of automation (Lee & See 2004; Parasuraman & Riley 1997). It shares the term trust engineering with Chen (2021), but with a different goal, and it takes its technical principles from Least Privilege (Saltzer & Schroeder 1975) and Zero Trust (NIST SP 800-207). A detailed comparison with prior work is given in the accompanying document [related-work.md](related-work.md).

## 3. The model in brief

This section summarizes only the quantities this paper needs. The full model, including the descriptive account, beliefs and psychological factors, is developed in Paper 1 (Rumpf 2026b) and in the long version (Chapters 2 to 6).

### 3.1 Trust as a directed graph of opinions

Trust is a subjective, context-dependent expectation about the behavior of an entity under uncertainty, combined with the willingness to make oneself vulnerable (Rousseau et al. 1998; Mayer et al. 1995). It is modeled as a directed graph G = (V, E). Entities are persons, groups, organizations, institutions, technical systems and AI agents. The relationship is directed, not symmetric, and changes over time. For technical objects without an assessment of their own, the relationship is one-sided. Agents that verify permissions themselves maintain edges of their own.

Each edge carries, per context c and dimension k, an opinion instead of a scalar:

```math
\omega_{A\to B,c,k} = (b,\; d,\; u,\; a), \qquad b + d + u = 1
```

b is trust, d distrust, u uncertainty, a the base rate (prior). The representation follows Subjective Logic (Jøsang 2016). The context is a triple of task domain, vulnerability type and relationship type; code execution and data access are task domains, and "technical" is a relationship type (long version, Section 3.2). The model uses four dimensions of trustworthiness: ability (competence), benevolence, integrity and predictability. For machines and agents, the dimensions correspond to performance, purpose and process according to Lee & See (2004).

### 3.2 Evidence accounts and temporal decay

Each edge maintains, per context and dimension, two evidence accounts: r for positive, s for negative evidence. Added to these are the base rate a and the prior strength W. The opinion follows from them:

```math
b = \frac{r}{r+s+W}, \qquad d = \frac{s}{r+s+W}, \qquad u = \frac{W}{r+s+W}, \qquad E = b + a\,u
```

E is the expected trustworthiness. u is evidential certainty read inversely: much evidence yields a small u. The model corresponds to the Beta Reputation System (Jøsang & Ismail 2002). E = 0.5 without any observation (u = 1) is distinguishable from E = 0.5 after a thousand mixed observations (u close to 0). A new edge starts with r = s = 0, i.e. u = 1 and E = a.

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

*Figure 1: Temporal decay according to Section 4.3 of the long version · illustrative parameters, 60 days*

Expected trust does not fall to zero but approaches the base rate. What is lost is the certainty of the assessment.

### 3.3 Discounting along chains

Trust information propagates via third parties. Normatively, however, trust is not transitive (Christianson & Harbison 1997). The model separates functional trust (B can do the task) from referral trust (C judges others well). A recommendation by C about B is discounted by A's referral trust in C:

```math
b_{A:B} = b_{A\to C}\,b_{C\to B}, \quad d_{A:B} = b_{A\to C}\,d_{C\to B}, \quad u_{A:B} = d_{A\to C} + u_{A\to C} + b_{A\to C}\,u_{C\to B}
```

This is the discounting operator of Subjective Logic. **Along a chain, trust can only decrease and uncertainty can only increase.** Own experience, another's statement and independently verified information remain separate kinds of evidence.

### 3.4 Source dependence

Repeated statements from dependent sources are not independent evidence. In the normative account, n repetitions from sources with dependence D count only as an effective sample:

```math
n_{\text{eff}} = \frac{n}{1 + (n-1)\,D}, \qquad \lim_{n\to\infty} n_{\text{eff}} = \frac{1}{D}
```

At D = 1 (one original source), n_eff = 1, no matter how often the statement appears. At D = 0.5, any number of repetitions reaches at most the value of two independent sources. The long version also keeps a descriptive account, in which perceived repetition raises trust without new evidence; the difference between the two accounts is the calibration gap Γ (long version, Sections 4.7 and 4.8; Paper 1 (Rumpf 2026b)). Decisions are made only on the basis of the normative account.

### 3.5 Three questions and the threshold rule

A trust decision breaks down into three checks that do not substitute for one another:

| Question | Checks | Model variable |
| --- | --- | --- |
| Identity | Who is the entity? | evidence on edge attribution |
| Authorization | May it trigger this action? | permission P |
| Factual correctness | Is the specific statement or request correct? | evidence on the event itself |

**A confirmed identity proves neither permission nor correctness.** Trust in the person proves none of the three.

An action x yields the benefit N for a legitimate request and the loss L in case of abuse. It is only worthwhile if the probability of legitimacy exceeds the threshold θ:

```math
\theta_x = \frac{L_x}{L_x + N_x}
```

The permission is granted if the normative trust minus an uncertainty penalty reaches the threshold:

```math
E^{\text{norm}} - \kappa\,u \;\ge\; \theta_x
```

κ is the risk aversion. Two consequences follow. The threshold depends only on the action, not on the person. And high uncertainty lowers the permission even when the expected value is high. Both consequences carry over to agents and machines directly: an approval policy is set per action class, and a node with little evidence receives little scope of action.

## 4. Positioning: trust engineering in Chen (2021)

The term trust engineering is already used by Chen (2021), though with a different goal. **Chen designs the trustee; this model designs the trust decision.** The two approaches complement each other. Chen describes trust as a four-place relation R(A, B, φ, G): A trusts B with respect to an action φ that serves a goal G. In this model, the goal is contained in the benefit N and loss L of the action.

Several of Chen's statements have a counterpart in the model that matters for agents:

| Statement in Chen (2021) | Counterpart in this model |
| --- | --- |
| Distrust can be the appropriate default stance, depending on environment, domain and consequences | base rate a per context; new agents start with u = 1 (Section 6) |
| The trustee is more an AI ecosystem of developers, operators and users than a single system | provider, model and operator as separate nodes; attestation (Sections 6 and 7) |
| Trust signals via outward appearance exploit weaknesses of judgment and do not make the system more trustworthy | signals without diagnosticity (q close to 0) only raise the descriptive account and enlarge Γ |
| Appreciation by trustors as part of the reward function of learning agents | no counterpart; such ratings would here be evidence to be weighted by independence D |

This implies a limit. In Chen's terms, this model mainly describes calibrated reliance and the permission derived from it. It does not specifically represent normative expectations and reactions such as the feeling of having been betrayed. It leaves open whether agents can be trustees in the full sense (Section 14).

## 5. Three directions of trust

Trust between humans, agents and machines runs in three directions. Each has its own core problem and main risk.

| Direction | Core problem | Main risk |
| --- | --- | --- |
| Human trusts agent | Calibration | Overtrust in fluent outputs, undertrust after individual errors |
| Agent trusts human or content | Authority of an instruction | injected instructions in content read, forged principals |
| Machine trusts machine | Identity, delegation, chains | overly broad rights, transitive chains, correlated verifiers |

The first direction concerns the human side of the edge: whether a person's trust matches the agent's actual performance. The second concerns which inputs an agent may treat as instructions. The third concerns identity, delegation and verification between technical nodes. Sections 6 to 8 develop what all three share; Section 9 treats each direction separately.

## 6. Establishing trust

Trust in a technical entity arises in six steps:

1. Verify identity independently, cryptographically rather than via self-disclosure.
2. Attribute credentials unambiguously.
3. Prove current possession or control.
4. Document provenance and state: which model, which version, which tools, which configuration.
5. Initially restrict permissions narrowly.
6. Adjust trust on the basis of verified behavior.

Steps 1 to 4 set only the base rate a. Evidence r arises only from verified results. **A correctly identified agent starts with u = 1.**

This is the evidence model's initial state (Section 3.2) applied to machines. Identity and attestation answer the first of the three questions, not the second or third. They set only the base rate a; evidence about whether B performs the task well arises only from verified results. Following Chen (2021), the trustee is often an ecosystem rather than a single system. Provider, model and operator are therefore separate nodes, and attestation concerns each of them.

Steps 1 to 4 also secure the anchor beneath the entire trust profile. Before A asks whether B is able, wishes well, keeps rules and acts consistently, one thing must be settled: is B really B? Whoever takes over the identity takes over not one dimension but the whole profile. The Zero Trust requirement to re-verify identity before every session (NIST SP 800-207) secures this anchor, not an individual dimension (long version, Section 13.5).

## 7. Mapping the model quantities to technical mechanisms

For technical nodes, every model quantity has a technical counterpart:

| Model variable | Technical counterpart (examples) |
| --- | --- |
| Edge attribution (identity) | mutual authentication, workload identities, signed requests |
| Base rate a | attestation of provider, model and runtime environment |
| Evidence accounts r, s | logged, verified task results per task type |
| Diagnosticity q | hard-to-forge evidence: signatures, reproducible results, passed tests |
| Forgetting factor λ | validity period of credentials, interval of re-attestation |
| Context c | task type and data class; evidence does not apply across contexts |
| Permission P | narrowly scoped, short-lived tokens and capabilities |
| Threshold θ | approval policy per action class |
| Source dependence D | diversity of verifiers: different model, different provider, human |
| Discounting in chains | delegation may only narrow rights, never extend them |

The principles correspond to Least Privilege (Saltzer & Schroeder 1975) and Zero Trust (NIST SP 800-207). What is new is the coupling to an evidence account with temporal decay.

Three points of the mapping deserve emphasis. First, diagnosticity q is the cost of faking a signal. A signature or a passed test is costly to forge; a confident self-description is not. Because g± is weighted by q, only evidence with high q moves the account appreciably. Second, context is the task type and data class. Evidence gathered in one task type does not apply to another, just as in the human case trust from one domain does not justify rights in another. Third, the discounting operator (Section 3.3) has a direct technical reading: since uncertainty can only grow along a chain, delegation may only narrow rights, never extend them.

## 8. Verifying recurrently

### 8.1 The re-verification interval

Without new evidence, uncertainty grows. If an edge has the amount of evidence n₀ = r + s at the time of the last verification, the following holds afterwards:

```math
u(t) = \frac{W}{W + n_0\,\lambda^{t}}
```

If an action class tolerates at most uncertainty u_max, the latest re-verification interval follows:

```math
t^{*} = \frac{\ln\!\left(\dfrac{W\,(1-u_{\max})}{u_{\max}\,n_0}\right)}{\ln \lambda}
```

The formula applies for 0 < λ < 1, n₀ > 0 and an edge that is still within the limit at the last verification, u(0) = W / (W + n₀) < u_max. If u(0) ≥ u_max, including a new edge with n₀ = 0, the formula gives no positive interval or none at all: verification is due immediately (t* = 0). Without forgetting (λ = 1), uncertainty stays at u(0); an edge within the limit then never crosses it through decay alone.

Worked example with illustrative values W = 2, n₀ = 40, λ = 0.9 per day:

| Action class | u_max | Re-verification interval t* |
| --- | --- | --- |
| low risk | 0.2 | about 15 days |
| high risk | 0.1 | about 8 days |

![Risky rights must be re-verified about twice as often](../../docs/figures/fig-08-reverification-interval.png)

*Figure 2: Re-verification interval according to Section 10.4 of the long version · illustrative parameters, two risk classes*

The curve shows how uncertainty grows without new evidence. Each risk class intersects it at a different point; that is where the next verification is due.

### 8.2 Consequences

Three rules follow:

- **Riskier permissions need shorter re-verification intervals.**
- More verified evidence lengthens the interval, but only logarithmically.
- A change of version or configuration turns the agent into a partly new node. The old evidence is to be devalued until new evidence is available.

The interval links two parts of the model. u_max is set by the action class, as the threshold θ is (Section 3.5). λ has its technical counterpart in the validity period of credentials and the interval of re-attestation (Section 7); t* states how long these may be at most. The values in the worked example are illustrative. How λ and u_max are set on a justified basis for agent systems is an open question (Section 13.3).

## 9. The three directions in detail

### 9.1 Human trusts agent

People use automation too much or too little (Parasuraman & Riley 1997). Even with reliable systems, monitoring declines (Parasuraman & Manzey 2010). Appropriate trust needs information about the performance, process and purpose of the system (Lee & See 2004).

Fluent, confident wording costs a language model nothing. **It has a diagnosticity q close to 0 and must not justify trust.** For design, this means:

- Keep trust per task type, not per agent.
- Form evidence only from verified results.
- Make uncertainty and evidence visible: sources, tests, intermediate steps.
- Stagger approvals by size of the loss: reversible actions with small L autonomously, irreversible ones with large L only with human approval.

According to hypothesis H9 (Section 11), repeated encounters with an agent may raise its subjective trust rating, i.e. the descriptive account, without new independent evidence. The design rules above aim at the normative account: only verified results enter it.

### 9.2 Agent trusts human or content

For an agent, every web page, email or file it reads is a source with unknown intent. The separation of the three questions (Section 3.5) applies strictly:

- **Identity:** Instructions are valid only from the authenticated principal via the designated channel.
- **Authorization:** **Content from tools is data and carries no authority to instruct.**
- **Correctness:** Even an authorized instruction is checked against action class and threshold.

In the model, an injected instruction is an impersonation: the content claims the principal's edge. In the long version's reading of attacks as operations on model variables, impersonation manipulates the edge attribution, and the attacker inherits the evidence r of another node (long version, Section 8.4). The countermeasure is to verify identity via an independent channel. This corresponds to the rule above that instructions are valid only from the authenticated principal via the designated channel.

### 9.3 Machine trusts machine

- **No transitivity.** If A trusts service B, this does not apply to B's subcontractor C. The discounting operator (Section 3.3) makes uncertainty grow with each link in the chain. In practice, this limits the permissible delegation depth.
- **Narrowing delegation.** Rights passed on are at most as broad as one's own and shorter in time.
- **Independent verifiers.** Two instances of the same model are correlated sources with D close to 1. A cross-check counts as second evidence only with a different model, a different data basis or a human verifier. The same applies to human verifiers (Paper 2 (Rumpf 2026c)).
- **Sybil resistance.** Many agreeing agents of the same origin count as one source (Douceur 2002).
- **Revocation.** Negative evidence on integrity withdraws permissions immediately and across contexts.
- **Evidence provenance.** Every entry in the evidence account carries source and type of verification, so that the account itself remains verifiable.

The point on independent verifiers follows from Section 3.4. At D = 1, n_eff = 1: a second instance of the same model adds no independent evidence, however confidently it agrees. The point on evidence provenance follows from the fact that a system that computes trust itself becomes a target of attack. Manipulated reputation scores are an attack on the model itself, because they place false evidence in the normative account (long version, Section 8.4).

### 9.4 Agents as critical co-thinkers

An agent can keep the normative account for people: count independent origins, recognize action classes, apply the verification rule. **In doing so, it assesses the evidential situation of a request, not the worth of a person.** This boundary is also legally required (Section 15).

## 10. Utility as a risk dimension for agents

### 10.1 Background: dimensions and security objectives

The long version compares the four trust dimensions with the security objectives of information security (long version, Chapter 13; treated in Paper 2 (Rumpf 2026c)). The proposal in brief (hypothesis H15, untested): the dimensions are properties of the actor B and determine the probability of occurrence; the security objectives are properties of the asset and determine the type of loss. Benevolence and confidentiality, integrity and data integrity, and predictability and availability are taken to form strong pairs. Competence has a weak effect on all three but has no counterpart in the triad of confidentiality, integrity and availability (CIA). **CIA presupposes that the system does the right thing and only measures whether it remains undisturbed while doing so.** This gap becomes practically relevant with AI agents.

### 10.2 Competence without a counterpart

If competence has no security objective, the question arises which one would correspond to it. The answer is Parker's utility: the result is present, unchanged and confidential, but unusable (Parker 1998). That is the typical damage of missing competence. Parker's example: data are encrypted, and afterwards the key is lost.

In ISO/IEC 27000 and in IT-Grundschutz, utility is not a security objective (ISO/IEC 27000:2018; BSI 2023). There it is a given value: an asset is considered because it is economically meaningful, and the protection requirement follows from this value. **Utility is an input to the protection requirements assessment, not an object of protection.**

In practice, an attack on utility is usually represented through availability. Ransomware makes data unusable by making them inaccessible. A lost key acts like an outage, an incompatible format like a lack of availability in usable form. For losses that arise later during operation, this mapping is usually sufficient.

It breaks down where the result is available and unchanged but inadequate from the start: wrong advice, a plausible but incorrect agent output, a correctly implemented but wrong specification. Such cases end up, as a makeshift, under data integrity, although nothing was falsified. There never was a correct state that could have been altered.

This yields a demarcation criterion. **Security models presuppose a target state and protect it against deviation. Competence concerns whether the target state is reached at all.** Utility is the point at which the trust model reaches beyond security risk into performance risk. It is not the trust model that is imprecise; the security model ends at this boundary.

Utility is already built into the model. The third of the three questions, factual correctness, asks exactly this: is the request or the result correct? And Chen's goal G in the four-place relation (Section 4) is the purpose the action is meant to serve. Utility means that φ actually serves G.

### 10.3 Why agents change the picture

The utility risk is not new. Classic software, too, can be available and unchanged and still fail to deliver what is needed, for example with a correctly implemented but wrong specification. There, however, it is dealt with before going live: through requirements analysis, testing and acceptance. After that, a deterministic system behaves the same for the same input, and the competence question counts as answered. The risk lies in the project, not in operation, and therefore drops out of the protection requirements assessment.

With AI agents, reaching the target state is itself probabilistic and situation-dependent. The difference is one of degree, but consequential: the risk arises anew with each execution, more frequently and harder to detect, and thereby moves from the project into operation. **An agent can be available, preserve confidentiality and be free of manipulation and still deliver unusable results**: through hallucination, plausible erroneous output or misinterpretation of the task. Fluent wording has a diagnosticity q close to 0 here (Section 9.1). A fixed reference against which data integrity could measure deviations is often missing; the NIST AI RMF notes that for AI systems a ground truth sometimes does not exist or is not available.

### 10.4 What the AI frameworks say

That the security models end here is shown by the AI frameworks themselves, which introduce the missing property separately. The NIST AI RMF 1.0 names seven characteristics of trustworthy AI and presents "valid and reliable" as a necessary condition and the basis of the others, while "secure and resilient" is defined separately via confidentiality, integrity and availability (NIST AI 100-1). Utility and CIA stand side by side there, not one within the other. The framework explicitly calls inaccurate but secure, privacy-enhanced and transparent systems undesirable and requires mechanisms to deactivate systems whose outputs are inconsistent with their intended use. The EU AI Act, in Art. 15, lists accuracy, robustness and cybersecurity as separate requirements for high-risk systems.

The security community confirms the shift as well. The OWASP Top 10 for LLM applications list Misinformation (LLM09:2025) as a risk in its own right: false but credible-seeming content, caused by hallucination and amplified by users' unverified trust (OWASP 2025). Next to it stands Excessive Agency (LLM06:2025), that is, too much functionality, permission and autonomy, whose consequences OWASP describes across confidentiality, integrity and availability. Together, the two show the pattern of the matrix: **Excessive Agency enlarges P and thus the loss in the CIA columns; Misinformation is a loss in the utility column without any CIA violation.**

Trust research supplies the matching conceptual axis. In Lee & See (2004), performance corresponds to competence, process to predictability and integrity, purpose to benevolence. Jacovi et al. (2021) conceive of human-AI trust as contractual: it refers to a contract about expected behavior and is warranted only if it is caused by actual trustworthiness. In this language, utility is the subject matter of the contract itself. The agent owes not only that it reveals nothing, falsifies nothing and is reachable, but that its result is fit for the purpose. Over- and undertrust (Parasuraman & Riley 1997) are thus utility risks on A's side.

**Conclusion of this section:** With agents, mapping utility onto availability or data integrity is no longer sufficient. An unusable but available and unchanged result is not an edge case but the characteristic failure pattern. Utility turns from a tacitly given input into a risk dimension that must be assessed, measured and monitored per task type. This supports the design rules in Section 9.1 and hypothesis H14 from the loss side and explains why competence evidence is kept per task type there.

![Three dimensions have a security objective, competence needs a fourth](../../docs/figures/fig-10-security-objectives.png)

*Figure 3: Trust dimensions and security objectives according to Sections 13.3 to 13.6 of the long version · strong and weak mappings, authenticity as an anchor*

The four strong mappings lie on the diagonal. Competence additionally has a weak effect on all other security objectives. Authenticity is not a fifth row but the condition that all four rows are actually attributed to B.

### 10.5 Implications for agents

**For the model.** For agents, utility is kept as a fourth column in protection requirements and risk assessments and backed by validation and monitoring evidence (rule S19, Section 12.2).

**Control and trust.** Security objectives are enforced through controls: encryption, rights, redundancy. Trust is needed where control is missing; Mayer et al. (1995) define it as vulnerability irrespective of the ability to monitor B. For the utility column of agents there are hardly any technical controls that reliably prevent a wrong but plausible result. What remains there is only calibrated trust, based on verified results per task type and human acceptance when L is high.

**For human-agent trust.** Users of agents need the reverse of the training for people. In training against social engineering, the first verification question is "Is B really B?" (Paper 2 (Rumpf 2026c)). An agent, however, can be authentic, available and confidential and still not be competent for the specific task. The verification question here is "Is this result fit for my purpose?", and it must be asked per result, not once per system. This verification, too, is subject to diffusion of responsibility: if several people share the acceptance of agent results, it needs a named role (Paper 2).

## 11. Hypotheses

The following hypotheses of the long version concern human-agent and machine-machine trust. They are hypotheses, not findings. H13 and H14 are untested effectiveness hypotheses. H15c is part of the structural hypothesis H15. H9 is a psychological hypothesis that the long version formulates for sources, organizations and agents; here it matters as it concerns agents.

**H9 – Transfer of familiarity to entities.** Repeated encounters with a source, organization or agent increase its subjective trust rating without new independent evidence. The effect grows with diminishing returns as frequency increases, decreases with accuracy focus and reverses with oversaturation.

**H13 – Temporal decay and re-verification.** Trust without new evidence returns to the base rate while uncertainty grows. Systems that couple permissions to aged evidence and re-verify staggered by risk limit losses better than systems with one-time granting of trust.

**H14 – Calibrated agent trust.** People calibrate their trust in agents better when evidence per task type from verified results is visible than when they see only the output. Cross-checking by correlated agents hardly improves error detection.

**H15c – Utility for agents.** For AI agents, utility becomes an independent risk dimension because reaching the target state is probabilistic. Unusable but available and unaltered results also exist in classical IT; there they are treated as a quality or project risk before going into operation. With agents they occur per execution, more frequently and harder to detect, and thus become an operational risk that can be mapped neither to availability nor to data integrity.

H15c refines the parent hypothesis H15: the four trust dimensions and the security objectives describe the same risk from two sides and form a matrix, not a mapping onto each other (long version, Section 11.3; Paper 2 (Rumpf 2026c)).

Evidence status as in the long version (Section 11.4). H15c has no row of its own; the row of H15 applies. Section references in the table refer to the long version.

| ID | Status | Supporting sources | Limiting sources |
| --- | --- | --- | --- |
| H9 | first preregistered evidence | Mattavelli et al. 2025; Montoya et al. 2017 | Brashier et al. 2020; Koch & Zerback 2013 |
| H13 | untested | derived from Section 4.3; NIST SP 800-207 | cost of frequent verification |
| H14 | untested | Lee & See 2004; Glikson & Woolley 2020 | automation complacency |
| H15 | conceptually grounded, untested | Mayer et al. 1995; Parker 1998; NIST AI 100-1 2023; OWASP 2025 | utility not established outside Parker; distinction from data integrity empirically blurred |

**Operationalization.** For each hypothesis, the following must be specified before testing: independent and dependent variables, confounders, measurement methods, expected direction and criteria for confirmation or refutation. Psychological hypotheses such as H9 and effectiveness hypotheses such as H13 and H14 need different designs. H15 is a structural hypothesis: it is tested by coding real incidents by dimension and security objective, not by an experiment. Effectiveness is always measured separately via discriminability and response bias (long version, Section 11.5).

## 12. Prediction and rules

### 12.1 Prediction V19

A news item about a category, for example AI content, shifts the base rate a of that category (long version, Section 12.4). One of the predictions derived from this concerns the authenticity of content:

| No. | Prediction | Derivation | Testable by |
| --- | --- | --- | --- |
| V19 | If the base rate for the authenticity of content falls, everyone accumulates evidence more slowly, and verified channels gain value. | q decreases for content evidence; u remains high throughout the graph | use of verified channels over time |

V19 is a derivation from the equations of the model, not a finding. The long version notes that V15 and V19 fit existing findings: blanket AI labeling also lowers the credibility of true headlines (Altay & Gilardi 2024), and pointing to possible forgery benefits the accused (Schiff et al. 2025). The prediction is qualitative. Quantitative statements need estimated parameters per population and context.

### 12.2 Rules

The long version derives twenty-four rules for information security (Chapter 14). Many are known as good practice, such as Zero Trust, least privilege and separation of duties. The model's contribution is a common justification, a ranking by size of the loss and a calculation rule for re-verification intervals. The following eight rules concern agents and machines most directly. They are derivations and, as a package, have not been empirically tested. Section references in the "Follows from" column refer to the long version.

| No. | Rule | Follows from | Implementation (examples) |
| --- | --- | --- | --- |
| S5 | A confirmation via the same channel is not a second piece of evidence. | D = 1 yields n_eff = 1 | call-back via a self-chosen number, never via details from the request |
| S6 | A majority counts only if independent. | n_eff is bounded by 1 / D | de-duplicate ratings, reports and agent votes by origin |
| S8 | Only costly signals count as proof. | q measures forgery costs | signatures, proofs of possession, pre-agreed code words |
| S9 | The evidence account itself is an object of protection. | manipulation of the model (8.4) | tamper-proof logs with provenance per entry |
| S10 | Trust ages and must be renewed. | temporal decay λ, re-verification interval t* | short-lived credentials, recertification of rights, locking of dormant accounts |
| S11 | Riskier rights are verified more often. | t* decreases with smaller u_max | staggered intervals per risk class |
| S13 | Trust is not transitive; chains are limited. | discounting operator (4.6) | verify suppliers and subcontractors individually, limit delegation depth |
| S19 | With agents, the result is checked for utility per task, not just the system for availability and integrity. | competence has no counterpart in the CIA triad (13.4, 13.6) | acceptance criteria per task type, samples of re-checked results, utility as a fourth column of the protection requirements assessment |

The rules map onto the sections of this paper. S5 and S6 follow from source dependence (Section 3.4) and apply to agent votes and cross-checks (Section 9.3). S8 follows from diagnosticity and excludes fluent wording as proof (Section 9.1). S9 follows from evidence provenance (Section 9.3). S10 and S11 follow from the re-verification interval (Section 8). S13 follows from discounting (Sections 3.3 and 9.3). S19 follows from the utility gap (Section 10). Among the four most important rules of the long version are S5 (together with S1) and S10: for a short list of risky actions, a verification via a second, self-chosen channel always applies, and every permission has an expiry date, staggered by risk. This selection follows from the ratio of size of the loss to effort in the model. It is a recommendation, not a finding.

## 13. Research plan

### 13.1 Phase 5: agent prototype

The long version plans six phases. Phase 5 concerns agents:

| Phase | Goal | Result |
| --- | --- | --- |
| 5 Agent prototype | evidence account with temporal decay and approval thresholds for an agent | testable implementation (H13, H14) |

One of the next development steps is to design a prototype of an agent evidence account with re-verification interval t* (H13). The technical verification of a simulation is not an empirical validation of the psychological model.

### 13.2 Simulation scenarios

Three of the long version's simulation scenarios concern agents:

- **Scenario 10.** Agent with a version change and renewed attestation (H13).
- **Scenario 11.** Cross-check by correlated and independent agents (H14).
- **Scenario 13.** Agent delivers available, unchanged but unusable results; comparison of detection with and without a utility check per task type (H15c).

Scenario 10 tests the third consequence of Section 8.2: a version change turns the agent into a partly new node. Scenario 11 tests whether cross-checks by correlated agents add evidence (Section 9.3). Scenario 13 tests whether a utility check per task type detects the failure pattern of Section 10.3. Any parameter values, like those in Section 8.1, are illustrative.

### 13.3 Open questions

**Practical**

- How are λ and u_max set on a justified basis for agent systems?
- How much independent evidence is needed for which action class?

**Psychological**

- Do familiarity effects transfer to organizations and agents (H9)?

**Theoretical**

- Does the model need a quantity of its own for normative expectations in order to distinguish trust from mere reliance (Chen 2021)?
- Is utility a security objective alongside confidentiality, integrity and availability, or a quantity outside security? Can the boundary between "never correct" and "altered later" be drawn empirically?

## 14. Limitations

- **Agent as trustee or as tool.** It remains open whether an agent is itself a trustee or a tool of its operator. This determines to whom benevolence and integrity are attributed.
- **Trust or reliance.** The model does not represent normative expectations separately. In Chen's (2021) distinction, it mainly describes calibrated reliance.
- **Quantification.** Even a triple of b, d and u is an abstraction. It has not been shown that human trust can be represented this completely.
- **Parameters.** The re-verification interval depends on W, n₀, λ and u_max. The values in Section 8 are illustrative. How they are set on a justified basis is open.
- **Utility is hardly established outside Parker.** Neither ISO/IEC 27000 nor IT-Grundschutz lists it as a security objective. The thesis rests on the parallel to "valid and reliable" in the AI RMF, not on a change to the standards.
- **Demarcation from data integrity and availability.** Whether a result was never correct or was altered later is not always observable, for example with poisoned training data. There, cells overlap.
- **Manipulation of the model.** A system that computes trust itself becomes a target of attack (rule S9).
- **No empirical test.** All parts of this paper are derivations from the model. The technical verification of a simulation is not an empirical validation.

## 15. Ethics and law

The model serves self-reflection, training, simulation and the assessment of technical systems. **It does not serve the assessment of persons for decisions by third parties.** When an agent keeps the normative account for people (Section 9.4), it assesses the evidential situation of a request, not the worth of a person. This boundary is also legally required.

- **EU AI Act, Art. 5(1)(c).** Prohibited are AI systems that evaluate persons over a period of time based on their social behavior or personal characteristics, where this leads to detrimental treatment in unrelated contexts or to disproportionate detrimental treatment. A graph that transfers group trust and carries it forward across contexts would come close to this prohibited practice.
- **GDPR Art. 22.** According to CJEU judgment C-634/21 (SCHUFA, 7 December 2023), the very creation of a score can be an automated decision.

Where the accounts concern persons, they assess the evidential situation of a request, not the worth of a person (long version, Sections 10.8 and 15.4). The legal classification is an initial assessment and does not replace a legal review.

## 16. Conclusion

Artificially generated content devalues the features from which people have so far read trustworthiness. For agents and machines, the evidence model offers a different basis. Trust is an evidential situation with three components: trust, distrust and ignorance. With technical nodes, these quantities, their temporal decay and the permission derived from them can be implemented explicitly.

Five points follow from the model. Identity and attestation set only the base rate; a correctly identified agent starts with u = 1. Each model quantity has a technical counterpart, and delegation may only narrow rights. The forgetting factor yields a latest re-verification interval, so riskier permissions are re-verified more often. The three directions of trust have different core problems: calibration, the authority of an instruction, and identity and delegation. And for agents, utility becomes a risk dimension of its own: an agent can be authentic, available and confidential and still not be competent for the specific task.

These statements are derivations. H13, H14 and H15c are untested, H9 has first preregistered evidence, and the rules have not been tested as a package. The next step is an agent prototype with an evidence account, temporal decay and approval thresholds, which makes H13 and H14 testable.

Trust is engineered: not because human trust could be reduced to an algorithm, but because decisions that rest on trust can be structured, verified and improved.

## References

- Rumpf, J. (2026a). Trust is Engineered. Working paper, version 0.6 (draft). https://github.com/JoeRu/trust-is-engineered
- Rumpf, J. (2026b). Trust is Engineered: An Evidence Model of Trust, Distrust and the Calibration Gap. Preprint, version 0.1 (draft), Paper 1 of 3. Zenodo. https://doi.org/10.5281/zenodo.23810447
- Rumpf, J. (2026c). Verification as a Public Good: Groups, Protection Delegation and Action-Bound Rules against Social Engineering. Preprint, version 0.2 (draft), Paper 2 of 3. Zenodo. https://doi.org/10.5281/zenodo.23813118
- Altay, S. & Gilardi, F. (2024). PNAS Nexus, 3(10), pgae403.
- Brashier, N. M., Eliseev, E. D. & Marsh, E. J. (2020). Cognition, 194, 104054.
- BSI (2023). IT-Grundschutz-Kompendium, Edition 2023, Glossar. Bundesamt für Sicherheit in der Informationstechnik. (wording on authenticity and *Verbindlichkeit* to be checked)
- Chen, M. (2021). Trust and Trust-Engineering in Artificial Intelligence Research: Theory and Praxis. Philosophy & Technology, 34, 1429–1447. https://doi.org/10.1007/s13347-021-00465-4 (checked against full text)
- Christianson, B. & Harbison, W. S. (1997). Why isn't trust transitive? Security Protocols Workshop, LNCS 1189, 171–176.
- CJEU, judgment of 7 December 2023, C-634/21 (SCHUFA).
- Douceur, J. R. (2002). The Sybil Attack. IPTPS, LNCS 2429.
- Glikson, E. & Woolley, A. W. (2020). Academy of Management Annals, 14(2), 627–660.
- ISO/IEC 27000:2018. Information technology – Security techniques – Information security management systems – Overview and vocabulary. (definitions to be checked against the text of the standard)
- Jacovi, A., Marasović, A., Miller, T. & Goldberg, Y. (2021). Formalizing Trust in Artificial Intelligence: Prerequisites, Causes and Goals of Human Trust in AI. FAccT '21, 624–635. https://doi.org/10.1145/3442188.3445923
- Jøsang, A. (2016). Subjective Logic. Springer.
- Jøsang, A. & Ismail, R. (2002). The Beta Reputation System. 15th Bled eConference.
- Koch, T. & Zerback, T. (2013). Journal of Communication, 63(6), 993–1010.
- Lee, J. D. & See, K. A. (2004). Human Factors, 46(1), 50–80.
- Mattavelli, S., Brambilla, M. & Unkelbach, C. (2025). Repeating statements increases source credibility. Personality and Social Psychology Bulletin, 52(9), 2724–2737.
- Mayer, R. C., Davis, J. H. & Schoorman, F. D. (1995). An Integrative Model of Organizational Trust. Academy of Management Review, 20(3), 709–734.
- Montoya, R. M. et al. (2017). Psychological Bulletin, 143(5), 459–498.
- NIST (2023). Artificial Intelligence Risk Management Framework (AI RMF 1.0). NIST AI 100-1. https://doi.org/10.6028/NIST.AI.100-1
- OWASP (2025). OWASP Top 10 for LLM Applications 2025 (LLM06 Excessive Agency, LLM09 Misinformation). OWASP Foundation.
- Parasuraman, R. & Manzey, D. H. (2010). Human Factors, 52(3), 381–410.
- Parasuraman, R. & Riley, V. (1997). Human Factors, 39(2), 230–253.
- Parker, D. B. (1998). Fighting Computer Crime: A New Framework for Protecting Information. Wiley. (page number for utility to be checked)
- Regulation (EU) 2016/679 (GDPR), Art. 9 and Art. 22.
- Regulation (EU) 2024/1689 (AI Act), Art. 5(1)(c); Art. 15 (accuracy, robustness and cybersecurity).
- Rose, S. et al. (2020). Zero Trust Architecture. NIST SP 800-207.
- Rousseau, D. M., Sitkin, S. B., Burt, R. S. & Camerer, C. (1998). Not so different after all. Academy of Management Review, 23(3), 393–404.
- Saltzer, J. H. & Schroeder, M. D. (1975). Proceedings of the IEEE, 63(9), 1278–1308.
- Schiff, K. J., Schiff, D. S. & Bueno, N. S. (2025). The Liar's Dividend. American Political Science Review, 119(1), 71–90.
- Spence, M. (1973). Job Market Signaling. Quarterly Journal of Economics, 87(3), 355–374.
