# What Is New: Calibrated Trust between Humans, Agents and Machines

> Working document accompanying [paper.md](paper.md); condensed from [related-work.md](related-work.md). Draft, 18 October 2026. Status markers as in the bibliography.

Paper 3 adds no new mechanism. It ties permissions of agents and machines to one quantity: an evidence account that decays toward the base rate. From this it derives a re-verification interval per action class and a common justification for known rules. The table compares each claim with the closest prior work named in the related-work document. All derivations are untested.

## Compared with prior work

| Prior work | What it already provides | What this paper adds | Overlap and reviewer risk |
| --- | --- | --- | --- |
| Lee & See 2004; Hoff & Bashir 2015 | Appropriate trust needs information on performance, process and purpose. Trust in automation has dispositional, situational and learned layers. | Trust per task type as an evidence account with explicit u and decay. Calibration as the gap between descriptive and normative account. | Adopted unchanged. The learned layer corresponds to the evidence account, the dispositional layer to the base rate. The paper should state this correspondence. |
| Zhang et al. 2020; Vasconcelos et al. 2023; S. Kim et al. 2024; S. Kim et al. 2025; Jacovi et al. 2021 | Confidence, explanations, sources and uncertainty wording change reliance on AI and LLM outputs, not always in the right direction. Trust is warranted only if actual trustworthiness causes it. | A reason in the model for one display (verified track record per task type) and for why fluent wording has q close to 0 (Section 9.1, H14 first part). | High. H14 is a further display condition in an existing paradigm. It is untested. |
| Blaze et al. 1996; Ellison et al. 1999 (SPKI, RFC 2693); Birgisson et al. 2014 (macaroons) | Trust management binds keys to permitted actions. SPKI intersects authorizations and validity periods along a chain. Macaroon caveats attenuate and confine credentials. | A reason for narrowing: under discounting, uncertainty only grows along a chain, which motivates a delegation-depth limit (S13). | Almost complete. Narrowing and time-bounded validity are formal SPKI and macaroon properties. Residual: validity coupled to an evidence account about the holder, not set by the issuer. |
| South et al. 2025; Huang et al. 2025; Ehtesham et al. 2025 (all preprints) | Authenticated, auditable delegation to agents via OAuth 2.0 and OpenID Connect. Verifiable agent identities with revocation. A comparison of agent protocols, including A2A Agent Cards. | The same delegation and identity questions inside one trust model. | High for machine→machine. These are the closest current proposals; the paper does not cite them yet. |
| NIST SP 800-207; Syed et al. 2022; Patel et al. 2016 | Zero trust drops implicit trust; continuous authentication monitors users after access. Syed et al. name trust and risk computation as an open challenge. | Re-verification of identity framed as securing the anchor of the whole trust profile (Section 6). | Medium. The paper itself says its principles correspond to Zero Trust and Least Privilege (Saltzer & Schroeder 1975). |
| Chakraborty & Ray 2006 (TrustBAC); Cheng et al. 2007 (Fuzzy MLS) | Permissions derived from trust levels based on behavior history, or from quantified risk and uncertainty. | (1) separate b, d and u, so a new node is "unknown", not "medium"; (2) threshold θ = L/(L+N) with penalty κu; (3) decay toward the base rate; the derived interval t*. | Substantial and under-cited. The strongest challenge to "coupling permissions to trust is new". Whether TrustBAC includes decay could not be checked from the abstract. |
| Coker et al. 2011; Birkholz et al. 2023 (RATS, RFC 9334) | Remote attestation with temporally fresh evidence. Appraisal policies judge freshness against an expiry threshold. | Attestation sets only the base rate a; evidence r comes only from verified results; a correctly identified agent starts with u = 1 (Section 6). A formula for the age limit from u_max and n₀. | Low to medium. The separation is a framing; its value is preventing "attested = trusted". "Version change = partly new node" is close to attestation practice and should be credited. |
| Jøsang & Ismail 2002; Jøsang 2016 | Beta evidence accounts with a forgetting factor; the discounting operator. | Nothing in the model itself; the paper uses them as its basis. | Must not be presented as a contribution. |
| Ramchurn et al. 2004; Teacy et al. 2006 (TRAVOS) | Probabilistic trust between agents from past interactions; handling of inaccurate third-party reputation. | (a) account tied to a permission threshold per action class, not partner selection; (b) a re-verification interval from decay. | Closest prior work for the evidence account. "What is new is the coupling" holds only with the emphasis on permissions. |
| Hoffman et al. 2009; Douceur 2002 | A taxonomy of attacks on reputation systems and defenses; the Sybil attack. | The account as an object of protection with provenance per entry (S9); agreeing agents of one origin count as one (S6). | Medium. S9 is in the spirit of Hoffman et al.; sybil resistance is established. |
| Greshake et al. 2023 | Indirect prompt injection: retrieved data acts as instructions and can steer API calls. | Injection read as impersonation of the principal's edge, in the same frame as social engineering (Section 9.2). | High for the rule "content is data". Only the framing is new. |
| Wallace et al. 2024; Debenedetti et al. 2024 (AgentDojo); Debenedetti et al. 2025 (CaMeL) | Instruction hierarchy as a training objective; a benchmark of 97 tasks and 629 security test cases; a system layer separating control and data flow with capabilities. | A correctness check against the action-class threshold, also for authorized instructions. | High. A unifying justification, not a mechanism. AgentDojo could serve as a test bed. |
| E. Kim et al. 2025; Zheng et al. 2023; Panickssery et al. 2024 | Substantial error correlation across more than 350 LLMs, even across providers for capable models. LLM judges show self-enhancement bias and favor their own outputs. | n_eff as the counting rule for agent votes and judges (S6, H14 second part). | Medium. Supports D close to 1 for same-model instances but qualifies "different provider" as a remedy. Wording must be weakened. |
| NIST 2023 (AI RMF); EU AI Act Art. 15; ISO/IEC 42001:2023 | "Valid and reliable" separate from "secure and resilient"; accuracy, robustness and cybersecurity as separate requirements; an AI management system standard. | Utility derived from the trust dimensions: competence has no CIA counterpart; verification per result and task type; move from project to operational risk (H15c, S19). | Medium. The frameworks already separate validity from security, and the paper says so. ISO/IEC 42001 checked only at the scope statement. |
| OWASP 2025; Parker 1998 | LLM06 Excessive Agency and LLM09 Misinformation as risks; utility as a security property next to CIA. | "Excessive Agency enlarges P; Misinformation is a loss in the utility column without a CIA violation." | Low to medium. The pairing is the paper's interpretation, not found in OWASP. |
| Chen 2021 | Trust engineering of the trustee; distrust as a possible default stance. | Engineering of the trust decision; u = 1 as the formal start state. | Low. Positioned in Section 4. |

## What remains new

- The re-verification interval t* from decay, accumulated evidence n₀ and a tolerable uncertainty u_max per action class, with its two rules: riskier rights need shorter intervals, and more evidence lengthens t* only logarithmically (Section 8, H13, S10, S11). This is the highest residual novelty, but thin. The related-work search found no peer-reviewed source that derives credential lifetimes from a decay model; that absence does not prove novelty.
- Coupling the validity of permissions to an evidence account about the holder's behavior, rather than to an issuer's setting (Section 7, S13).
- The separation of state evidence (base rate a, from attestation) from behavioral evidence (r, s), with u = 1 as the start state (Section 6).
- One vocabulary and the same three checks (identity, authorization, correctness) across the three trust directions (Sections 5 and 9).
- Utility for agents as a consequence of the trust dimensions, with evidence kept per task type (Section 10, H15c, S19). H15c remains a hypothesis.

## What is not new

- The decaying Beta evidence account and the discounting operator (Jøsang & Ismail 2002; Jøsang 2016), and probabilistic trust between agents (Teacy et al. 2006).
- Narrowing delegation and time-bounded validity (Ellison et al. 1999; Birgisson et al. 2014), Least Privilege and Zero Trust.
- Deriving permissions from behavior history or quantified risk (Chakraborty & Ray 2006; Cheng et al. 2007).
- "Content from tools is data" (Greshake et al. 2023) and defenses that separate control from data (Debenedetti et al. 2025).
- Correlated LLM errors and self-preference of LLM judges (E. Kim et al. 2025; Panickssery et al. 2024).
- The separation of validity from security in AI frameworks (NIST 2023; EU AI Act Art. 15).

## Before submission

- Cite TrustBAC and Fuzzy MLS and narrow the novelty claim to the b/d/u separation, the threshold with uncertainty penalty, decay and t*.
- Add Hoff & Bashir 2015, the trust-management works, RATS and the agent-delegation preprints to the relevant sections, and state the attestation analogy for version changes.
- Weaken "different model, different provider" as a remedy for correlated verifiers, citing E. Kim et al. 2025.
- Run a targeted search in access-control and trust-management venues (SACMAT, CCS, ESORICS, IFIPTM) for decay-based credential lifetimes.
- Check ISO/IEC 42001:2023 against the text of the standard before any statement about its content. All new sources were read only at abstract level.

## References

- Birgisson, A., Politz, J. G., Erlingsson, Ú., Taly, A., Vrable, M. & Lentczner, M. (2014). Macaroons: Cookies with Contextual Caveats for Decentralized Authorization in the Cloud. Network and Distributed System Security Symposium (NDSS 2014). https://doi.org/10.14722/ndss.2014.23212 (new, secondary citation)
- Birkholz, H., Thaler, D., Richardson, M., Smith, N. & Pan, W. (2023). Remote ATtestation procedureS (RATS) Architecture. RFC 9334, IETF. https://doi.org/10.17487/RFC9334 (new, secondary citation)
- Blaze, M., Feigenbaum, J. & Lacy, J. (1996). Decentralized Trust Management. Proceedings 1996 IEEE Symposium on Security and Privacy, 164–173. https://doi.org/10.1109/SECPRI.1996.502679 (new, secondary citation)
- Chakraborty, S. & Ray, I. (2006). TrustBAC: Integrating Trust Relationships into the RBAC Model for Access Control in Open Systems. Proceedings of the 11th ACM Symposium on Access Control Models and Technologies (SACMAT '06), 49. https://doi.org/10.1145/1133058.1133067 (new, secondary citation)
- Chen, M. (2021). Trust and Trust-Engineering in Artificial Intelligence Research: Theory and Praxis. Philosophy & Technology, 34, 1429–1447. https://doi.org/10.1007/s13347-021-00465-4 (checked against full text)
- Cheng, P.-C., Rohatgi, P., Keser, C., Karger, P. A., Wagner, G. M. & Reninger, A. S. (2007). Fuzzy Multi-Level Security: An Experiment on Quantified Risk-Adaptive Access Control. 2007 IEEE Symposium on Security and Privacy (SP '07), 222–230. https://doi.org/10.1109/SP.2007.21 (new, secondary citation)
- Coker, G., Guttman, J., Loscocco, P., Herzog, A., Millen, J., O'Hanlon, B., Ramsdell, J., Segall, A., Sheehy, J. & Sniffen, B. (2011). Principles of remote attestation. International Journal of Information Security, 10(2), 63–81. https://doi.org/10.1007/s10207-011-0124-7 (new, secondary citation)
- Debenedetti, E., Zhang, J., Balunović, M., Beurer-Kellner, L., Fischer, M. & Tramèr, F. (2024). AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents. Advances in Neural Information Processing Systems 37, 82895–82920. https://doi.org/10.52202/079017-2636 (new, secondary citation)
- Debenedetti, E., Shumailov, I., Fan, T., Hayes, J., Carlini, N., Fabian, D., Kern, C., Shi, C., Terzis, A. & Tramèr, F. (2025). Defeating Prompt Injections by Design. arXiv preprint arXiv:2503.18813. (new, secondary citation)
- Douceur, J. R. (2002). The Sybil Attack. IPTPS, LNCS 2429.
- Ehtesham, A., Singh, A., Gupta, G. K. & Kumar, S. (2025). A survey of agent interoperability protocols: Model Context Protocol (MCP), Agent Communication Protocol (ACP), Agent-to-Agent Protocol (A2A), and Agent Network Protocol (ANP). arXiv preprint arXiv:2505.02279. (new, secondary citation)
- Ellison, C., Frantz, B., Lampson, B., Rivest, R., Thomas, B. & Ylonen, T. (1999). SPKI Certificate Theory. RFC 2693, IETF (Experimental). https://doi.org/10.17487/RFC2693 (new, secondary citation)
- Greshake, K., Abdelnabi, S., Mishra, S., Endres, C., Holz, T. & Fritz, M. (2023). Not What You've Signed Up For: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection. Proceedings of the 16th ACM Workshop on Artificial Intelligence and Security (AISec '23), 79–90. https://doi.org/10.1145/3605764.3623985 (new, secondary citation)
- Hoff, K. A. & Bashir, M. (2015). Trust in Automation: Integrating Empirical Evidence on Factors That Influence Trust. Human Factors, 57(3), 407–434. https://doi.org/10.1177/0018720814547570 (new, secondary citation)
- Hoffman, K., Zage, D. & Nita-Rotaru, C. (2009). A survey of attack and defense techniques for reputation systems. ACM Computing Surveys, 42(1), 1–31. https://doi.org/10.1145/1592451.1592452 (new, secondary citation)
- Huang, K., Narajala, V. S., Yeoh, J., Ross, J., Raskar, R., Harkati, Y., Huang, J., Habler, I. & Hughes, C. (2025). A Novel Zero-Trust Identity Framework for Agentic AI: Decentralized Authentication and Fine-Grained Access Control. arXiv preprint arXiv:2505.19301. (new, secondary citation)
- ISO/IEC 42001:2023. Information technology – Artificial intelligence – Management system. ISO/IEC JTC 1/SC 42. (new, secondary citation)
- Jacovi, A., Marasović, A., Miller, T. & Goldberg, Y. (2021). Formalizing Trust in Artificial Intelligence: Prerequisites, Causes and Goals of Human Trust in AI. FAccT '21, 624–635. https://doi.org/10.1145/3442188.3445923
- Jøsang, A. (2016). Subjective Logic. Springer.
- Jøsang, A. & Ismail, R. (2002). The Beta Reputation System. 15th Bled eConference.
- Kim, E. M., Garg, A., Peng, K. & Garg, N. (2025). Correlated Errors in Large Language Models. Proceedings of the 42nd International Conference on Machine Learning, PMLR 267, 30038–30066. (new, secondary citation)
- Kim, S. S. Y., Liao, Q. V., Vorvoreanu, M., Ballard, S. & Vaughan, J. W. (2024). "I'm Not Sure, But...": Examining the Impact of Large Language Models' Uncertainty Expression on User Reliance and Trust. FAccT '24, 822–835. https://doi.org/10.1145/3630106.3658941 (new, secondary citation)
- Kim, S. S. Y., Vaughan, J. W., Liao, Q. V., Lombrozo, T. & Russakovsky, O. (2025). Fostering Appropriate Reliance on Large Language Models: The Role of Explanations, Sources, and Inconsistencies. CHI '25, 1–19. https://doi.org/10.1145/3706598.3714020 (new, secondary citation)
- Lee, J. D. & See, K. A. (2004). Human Factors, 46(1), 50–80.
- NIST (2023). Artificial Intelligence Risk Management Framework (AI RMF 1.0). NIST AI 100-1. https://doi.org/10.6028/NIST.AI.100-1
- OWASP (2025). OWASP Top 10 for LLM Applications 2025 (LLM06 Excessive Agency, LLM09 Misinformation). OWASP Foundation.
- Panickssery, A., Bowman, S. R. & Feng, S. (2024). LLM Evaluators Recognize and Favor Their Own Generations. Advances in Neural Information Processing Systems 37, 68772–68802. https://doi.org/10.52202/079017-2197 (new, secondary citation)
- Parker, D. B. (1998). Fighting Computer Crime: A New Framework for Protecting Information. Wiley. (page number for utility to be checked)
- Patel, V. M., Chellappa, R., Chandra, D. & Barbello, B. (2016). Continuous User Authentication on Mobile Devices: Recent progress and remaining challenges. IEEE Signal Processing Magazine, 33(4), 49–61. https://doi.org/10.1109/MSP.2016.2555335 (new, secondary citation)
- Ramchurn, S. D., Huynh, D. & Jennings, N. R. (2004). Trust in multi-agent systems. The Knowledge Engineering Review, 19(1), 1–25. https://doi.org/10.1017/S0269888904000116 (new, secondary citation)
- Regulation (EU) 2024/1689 (AI Act), Art. 5(1)(c); Art. 15 (accuracy, robustness and cybersecurity).
- Rose, S. et al. (2020). Zero Trust Architecture. NIST SP 800-207.
- Saltzer, J. H. & Schroeder, M. D. (1975). Proceedings of the IEEE, 63(9), 1278–1308.
- South, T., Marro, S., Hardjono, T., Mahari, R., Whitney, C. D., Greenwood, D., Chan, A. & Pentland, A. (2025). Authenticated Delegation and Authorized AI Agents. arXiv preprint arXiv:2501.09674. (new, secondary citation)
- Syed, N. F., Shah, S. W., Shaghaghi, A., Anwar, A., Baig, Z. & Doss, R. (2022). Zero Trust Architecture (ZTA): A Comprehensive Survey. IEEE Access, 10, 57143–57179. https://doi.org/10.1109/ACCESS.2022.3174679 (new, secondary citation)
- Teacy, W. T. L., Patel, J., Jennings, N. R. & Luck, M. (2006). TRAVOS: Trust and Reputation in the Context of Inaccurate Information Sources. Autonomous Agents and Multi-Agent Systems, 12(2), 183–198. https://doi.org/10.1007/s10458-006-5952-x (new, secondary citation)
- Vasconcelos, H., Jörke, M., Grunde-McLaughlin, M., Gerstenberg, T., Bernstein, M. S. & Krishna, R. (2023). Explanations Can Reduce Overreliance on AI Systems During Decision-Making. Proceedings of the ACM on Human-Computer Interaction, 7(CSCW1), 1–38. https://doi.org/10.1145/3579605 (new, secondary citation)
- Wallace, E., Xiao, K., Leike, R., Weng, L., Heidecke, J. & Beutel, A. (2024). The Instruction Hierarchy: Training LLMs to Prioritize Privileged Instructions. arXiv preprint arXiv:2404.13208. (new, secondary citation)
- Zhang, Y., Liao, Q. V. & Bellamy, R. K. E. (2020). Effect of confidence and explanation on accuracy and trust calibration in AI-assisted decision making. FAT* '20, 295–305. https://doi.org/10.1145/3351095.3372852 (new, secondary citation)
- Zheng, L., Chiang, W.-L., Sheng, Y., Zhuang, S., Wu, Z., Zhuang, Y., Lin, Z., Li, Z., Li, D., Xing, E., Zhang, H., Gonzalez, J. & Stoica, I. (2023). Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena. Advances in Neural Information Processing Systems 36, 46595–46623. https://doi.org/10.52202/075280-2020 (new, secondary citation)
