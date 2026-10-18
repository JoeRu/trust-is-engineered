# What Is New: An Evidence Model of Trust, Distrust and the Calibration Gap

> Working document accompanying [paper.md](paper.md); condensed from [related-work.md](related-work.md). Draft, 18 October 2026. Status markers as in the bibliography.

The paper proposes no new operators. Its contribution is one evidence model that keeps trust, distrust and uncertainty separate, runs a normative and a descriptive account on the same events, defines their difference Γ as the calibration gap, and reads social-engineering techniques as operations on model quantities. The table compares this with the closest prior work. Section numbers refer to paper.md.

## Compared with prior work

| Prior work | What it already provides | What this paper adds | Overlap and reviewer risk |
| --- | --- | --- | --- |
| Marsh 1994 | An early formalization of trust as a computational concept. | Uses the computational line as a normative reference for human trust, not to produce a score for decisions. | Low. Not yet cited in the paper. |
| Jøsang & Ismail 2002 (Beta Reputation System) | Positive and negative evidence counts of a beta distribution; a forgetting factor; discounting of feedback by the reputation of the rater (both checked in its full text for the related-work document). | Composite event weight g± from ϱ, q, w±, r(e,c) and v (5.3); closed-form readings "decay to ignorance", half-life t½ and u_min; predictions V10–V13 from them. | High for the mechanism, low for the readings. Section 5.3 reads as if decay were added by the model; it must say that forgetting is already part of the Beta Reputation System. |
| Jøsang 2016 (Subjective Logic) | Opinions (b, d, u, a) with operators for discounting and fusion. | Indexing of each opinion by a context triple and four dimensions (4.1, 4.2, 3.4); use of u vs d to separate ignorance from ambivalence and bubble from chamber (3.2). | High. Formalism and discounting operator (5.6) are adopted; present them as adoption plus indexing. |
| Wang & Singh 2010 | Trust as certainty from evidence; certainty grows with evidence and falls with conflict; discounting and combining trust reports. | u read inversely as evidential certainty inside a two-account model. | Closest formal precedent for 5.1; not yet cited. |
| Teacy et al. 2006 (TRAVOS) | Probabilistic trust from past interactions; third-party reputation that may be inaccurate. | Weighting of sources by independence D and diagnosticity q inside the normative account (5.7). | Computational counterpart of source weighting; should be cited at 5.7. |
| Guha et al. 2004 | Propagation of trust and distrust in a directed rating network; by their account the first to include distrust. | Descriptive claim that people discount referrals less than dependence requires, least for the in-group (H4, H4a). | Precedent for propagating distrust separately; H4 is only "normatively grounded, descriptively partly supported". |
| Castelfranchi & Falcone 2010 | Trust as a mental attitude of beliefs and goals and as a decision to rely. | Separation of evaluation from decision (3.1, 7.1) with beliefs as filters on a, W and v (6.3), not a belief-goal structure. | Agents reviewers will ask why the socio-cognitive model is not the descriptive account. Answer from identifiability (12), not superiority. |
| Mayer et al. 1995; Rousseau et al. 1998 | Trust as willingness to be vulnerable; separation of trust from risk taking; ability, benevolence, integrity; cross-disciplinary definition. | Coupling of the decision layer to the opinion: threshold θ = L/(L+N), uncertainty penalty κu, verification rule (7.2, 7.3); "threshold depends only on the action". | Low–medium. Definition and dimensions are adopted. The θ formula is standard decision theory and should not be presented as derived. |
| Lewicki et al. 1998; McKnight & Chervany 2001 | Trust and distrust as separate dimensions or constructs that can operate at the same time. | Reading of the two dimensions as b and d of one opinion (3.2, Figure 1). | High. The distinction is old. Because b + d + u = 1, "ambivalence" means much evidence of both signs; treat the mapping as a modeling choice, not a rendering of Lewicki (open question in 11.3). |
| Lee & See 2004; Parasuraman & Riley 1997 | Appropriate reliance: trust should match capability; misuse and disuse as over- and underreliance; performance, process, purpose. | Reference is evidence-justified trust, not true reliability; both accounts on one event stream; Γ signed, per edge, context, dimension and time; each miscalibration mechanism a named term (5.8). | Medium–high. Γ > 0 and Γ < 0 restate over- and undertrust. Reviewers will ask how E^desc is measured and whether Γ is identifiable. Γ must not be presented as a measured quantity. |
| Wischnewski et al. 2023 | Review of 96 publications on calibrating trust in automated systems: how calibration is measured and how interventions are designed. | No measurement yet; Γ needs one. | The paper has no measurement design for Γ; cite in limitations and research plan. |
| Guo & Yang 2021 | Bayesian model of trust dynamics in human–robot teaming against a rational updater; three types of deviation. | Evidence from people and sources with dependence and diagnosticity, not observed robot performance. | Structurally close to the normative/descriptive split. Must be cited at 5.8 with the difference in object. |
| Hoff & Bashir 2015 | Dispositional, situational and learned layers of trust in automation. | Assignment of each factor to one model variable and one time scale (6). | Medium. Layering overlaps; cite the correspondence instead of presenting the levels as new. |
| Chang et al. 2010 | Trustworthiness as a belief about reciprocation, starting from initial judgments and updated by experience. | Prior from group and disposition, then evidence learning (5.2, 5.4). | Closest empirical-computational precedent; missing from the long version. Learning rate g/(n+g) and buffering are standard beta-updating properties. |
| Enke & Zimmermann 2019; DeMarzo et al. 2003; Eyster & Rabin 2010 | Correlation neglect in experiments; persuasion bias (failure to adjust for repetitions in a network); naive herding on redundant signals. | Correlation neglect, persuasion bias and naive herding read as one quantity: the part of Γ due to dependence D, which enters only the normative account (5.7). | Medium. The failure to discount repeated information is already modeled formally. Without these citations the descriptive account looks like a re-invention of persuasion bias. |
| Kish 1965 | Design-effect correction for clustered samples (attribution to be confirmed). | n_eff = n/(1 + (n−1)D) used inside a trust account, with D in the role of an intra-cluster correlation. | The form of n_eff is presented without attribution. |
| DeGroot 1974; Hegselmann & Krause 2002; Golub & Jackson 2010 | Consensus by pooling; bounded confidence; conditions under which naive averaging reaches the truth. | Different object: trust in a source from evidence about it; group anchoring only as a prior (4.4). | Medium. Network predictions V20 and V21 lack an opinion-dynamics baseline. |
| Hoffman et al. 2009; Douceur 2002 | Attacks on reputation systems classified by the component they target; the Sybil attack on counting identities as independent. | Social-engineering techniques against human evaluation mapped onto one variable set (8.4); calibration attacks (Γ) separated from abuse attacks (P) (8.2). | Medium. Same method as Hoffman et al. 2009. No direct precedent for the variable mapping in the abstracts seen; the search was not systematic. |
| Mouton et al. 2014; Wang, Sun & Zhu 2020 | A social-engineering attack framework and a definition of social engineering. | A quantitative evidence reading of the techniques; neither abstract describes one. | Without them, Chapter 8 looks unconnected to the social-engineering literature. |

## What remains new

- The integration of dependence D and diagnosticity q into the evidence weight of a trust account, so that repetition from dependent sources does not raise normative trust (5.3, 5.7). This is an integration, not a new mechanism.
- Two accounts on one event stream and their signed difference Γ per edge, context, dimension and time, with each miscalibration mechanism as a separately parameterized term: the familiarity term φ(1−m)ln(1+R), neglect of D, belief-colored valence (5.7, 5.8).
- The distinction between abuse attacks and calibration attacks, and the mapping of social-engineering techniques onto model variables (8.2, 8.4). This is the weakest-evidenced claim: conceptual, untested, based on a non-systematic search.
- The closed-form readings of decay (t½, u_min, "decay to ignorance") and the list of qualitative predictions V1–V21 with a named test per prediction (5.3, 10). The predictions are derivations, not findings.
- The assignment of psychological factors to one variable and one time scale each, and the conditioning of asymmetry on dimension and deception (6, H5a). Both are modeling choices; H5a is a hypothesis, "partly supported".

## What is not new

- The opinion triple, evidence accounts with base rate and prior strength, the forgetting factor and the discounting operator are adopted from Jøsang & Ismail 2002 and Jøsang 2016.
- The separation of trust and distrust is established (Lewicki et al. 1998; McKnight & Chervany 2001; Guha et al. 2004).
- The calibration idea, including both error directions, comes from Lee & See 2004 and Parasuraman & Riley 1997.
- Buffering and structural asymmetry follow from the learning rate of beta updating (Bush–Mosteller, Rescorla–Wagner, named in the paper). The learning trap is Denrell's mechanism (Denrell 2005).
- The threshold θ = L/(L+N) is elementary expected-loss reasoning. The definition and dimensions follow Mayer et al. 1995 and Rousseau et al. 1998.
- Correlation neglect, persuasion bias and naive herding are formally modeled already (Enke & Zimmermann 2019; DeMarzo et al. 2003; Eyster & Rabin 2010).

## Before submission

- Rewrite 5.3 to state that the Beta Reputation System already contains forgetting and rater discounting. Attribute the form of n_eff to the design effect after checking Kish 1965.
- Cite Wang & Singh 2010 (5.1), Teacy et al. 2006 and DeMarzo et al. 2003 and Eyster & Rabin 2010 (5.7), Guha et al. 2004 (5.6), Guo & Yang 2021 (5.8), Hoff & Bashir 2015 (6), Chang et al. 2010 (5.4), Hoffman et al. 2009 and Mouton et al. 2014 (8.2–8.4). Add Merdes, von Sydow & Hahn 2021 to the limitation "normative standard".
- Narrow the trust–distrust claim: present the b/d mapping as a modeling choice and state the b + d + u = 1 mismatch.
- Name DeGroot-type and bounded-confidence models as baselines for V20, V21 and simulation scenario 7.
- Repeat a targeted search for prior work applying Subjective Logic or beta evidence models to human susceptibility to social engineering. It would be the most damaging overlap for the calibration-attack framing. Read de Visser et al. 2020 before citing it.

## References

- Castelfranchi, C. & Falcone, R. (2010). Trust Theory. Wiley.
- Chang, L. J., Doll, B. B., van 't Wout, M., Frank, M. J. & Sanfey, A. G. (2010). Seeing is believing: Trustworthiness as a dynamic belief. Cognitive Psychology, 61(2), 87–105. https://doi.org/10.1016/j.cogpsych.2010.03.001 (new, secondary citation)
- de Visser, E. J., Peeters, M. M. M., Jung, M. F., Kohn, S., Shaw, T. H., Pak, R. & Neerincx, M. A. (2020). Towards a Theory of Longitudinal Trust Calibration in Human–Robot Teams. International Journal of Social Robotics, 12(2), 459–478. https://doi.org/10.1007/s12369-019-00596-x (new, to be checked)
- DeGroot, M. H. (1974). Reaching a Consensus. Journal of the American Statistical Association, 69(345), 118–121. https://doi.org/10.1080/01621459.1974.10480137 (new, secondary citation)
- DeMarzo, P. M., Vayanos, D. & Zwiebel, J. (2003). Persuasion Bias, Social Influence, and Unidimensional Opinions. Quarterly Journal of Economics, 118(3), 909–968. https://doi.org/10.1162/00335530360698469 (new, secondary citation)
- Denrell, J. (2005). Psychological Review, 112(4), 951–978.
- Douceur, J. R. (2002). The Sybil Attack. IPTPS, LNCS 2429.
- Enke, B. & Zimmermann, F. (2019). Review of Economic Studies, 86(1), 313–332.
- Eyster, E. & Rabin, M. (2010). Naïve Herding in Rich-Information Settings. American Economic Journal: Microeconomics, 2(4), 221–243. https://doi.org/10.1257/mic.2.4.221 (new, secondary citation)
- Golub, B. & Jackson, M. O. (2010). Naïve Learning in Social Networks and the Wisdom of Crowds. American Economic Journal: Microeconomics, 2(1), 112–149. https://doi.org/10.1257/mic.2.1.112 (new, secondary citation)
- Guha, R., Kumar, R., Raghavan, P. & Tomkins, A. (2004). Propagation of trust and distrust. Proceedings of the 13th International Conference on World Wide Web (WWW '04), 403–412. https://doi.org/10.1145/988672.988727 (new, secondary citation)
- Guo, Y. & Yang, X. J. (2021). Modeling and Predicting Trust Dynamics in Human–Robot Teaming: A Bayesian Inference Approach. International Journal of Social Robotics, 13(8), 1899–1909. https://doi.org/10.1007/s12369-020-00703-3 (new, secondary citation)
- Hegselmann, R. & Krause, U. (2002). Opinion dynamics and bounded confidence: models, analysis and simulation. Journal of Artificial Societies and Social Simulation, 5(3). https://www.jasss.org/5/3/2.html (new, secondary citation)
- Hoff, K. A. & Bashir, M. (2015). Trust in Automation: Integrating Empirical Evidence on Factors That Influence Trust. Human Factors, 57(3), 407–434. https://doi.org/10.1177/0018720814547570 (new, secondary citation)
- Hoffman, K., Zage, D. & Nita-Rotaru, C. (2009). A survey of attack and defense techniques for reputation systems. ACM Computing Surveys, 42(1), 1–31. https://doi.org/10.1145/1592451.1592452 (new, secondary citation)
- Jøsang, A. (2016). Subjective Logic. Springer.
- Jøsang, A. & Ismail, R. (2002). The Beta Reputation System. 15th Bled eConference.
- Kish, L. (1965). Survey Sampling. Wiley. (new, to be checked)
- Lee, J. D. & See, K. A. (2004). Human Factors, 46(1), 50–80.
- Lewicki, R. J., McAllister, D. J. & Bies, R. J. (1998). Academy of Management Review, 23(3), 438–458.
- Marsh, S. (1994). Formalising Trust as a Computational Concept. PhD thesis, University of Stirling.
- Mayer, R. C., Davis, J. H. & Schoorman, F. D. (1995). An Integrative Model of Organizational Trust. Academy of Management Review, 20(3), 709–734.
- McKnight, D. H. & Chervany, N. L. (2001). Trust and Distrust Definitions: One Bite at a Time. In R. Falcone, M. Singh & Y.-H. Tan (Eds.), Trust in Cyber-societies, LNAI 2246, 27–54. Springer. https://doi.org/10.1007/3-540-45547-7_3 (new, secondary citation)
- Merdes, C., von Sydow, M. & Hahn, U. (2021). Formal models of source reliability. Synthese, 198(Suppl. 23), 5773–5801. https://doi.org/10.1007/s11229-020-02595-2 (new, secondary citation)
- Mouton, F., Malan, M. M., Leenen, L. & Venter, H. S. (2014). Social engineering attack framework. 2014 Information Security for South Africa (ISSA), 1–9. https://doi.org/10.1109/ISSA.2014.6950510 (new, secondary citation)
- Parasuraman, R. & Riley, V. (1997). Human Factors, 39(2), 230–253.
- Rousseau, D. M., Sitkin, S. B., Burt, R. S. & Camerer, C. (1998). Not so different after all. Academy of Management Review, 23(3), 393–404.
- Teacy, W. T. L., Patel, J., Jennings, N. R. & Luck, M. (2006). TRAVOS: Trust and Reputation in the Context of Inaccurate Information Sources. Autonomous Agents and Multi-Agent Systems, 12(2), 183–198. https://doi.org/10.1007/s10458-006-5952-x (new, secondary citation)
- Wang, Y. & Singh, M. P. (2010). Evidence-based trust: A mathematical model geared for multiagent systems. ACM Transactions on Autonomous and Adaptive Systems, 5(4), 1–28. https://doi.org/10.1145/1867713.1867715 (new, secondary citation)
- Wang, Z., Sun, L. & Zhu, H. (2020). Defining Social Engineering in Cybersecurity. IEEE Access, 8, 85094–85115. https://doi.org/10.1109/ACCESS.2020.2992807 (new, secondary citation)
- Wischnewski, M., Krämer, N. & Müller, E. (2023). Measuring and Understanding Trust Calibrations for Automated Systems: A Survey of the State-Of-The-Art and Future Directions. Proceedings of the 2023 CHI Conference on Human Factors in Computing Systems, 1–16. https://doi.org/10.1145/3544548.3581197 (new, secondary citation)
