# Managing Product Development — Submission 1 Feedback

## Submission Result

- **Project:** Managing Product Development
- **Project due date:** January 19, 2027
- **Submission date:** November 15, 2026
- **Result:** Submission Did Not Pass
- **Specification review:** 1 specification requires changes

Please review the feedback details to understand the reasons for the failure. You can resubmit the project when you have made the necessary updates.

### Required Change

**Prioritize the functional test cases.** The reviewer identified that all functional test cases are marked as P1, making it difficult to distinguish truly launch-blocking functionality from lower-risk functionality.

### Specification Review Summary

| Area | Specification | Result |
| --- | --- | --- |
| Test Plan | Write test cases for functional requirements | Requires changes |
| Test Plan | Write test cases for non-functional requirements | Passed |
| Dogfood Survey | Create a dogfood survey | Passed |
| Fire Drills & Prioritization | Prioritize effectively | Passed |
| Fire Drills & Prioritization | Identify correct parties and communicates appropriately | Passed |
| Fire Drills & Prioritization | Communicate with concise, actionable key messages | Passed |
| Go No Go | Launch recommendation | Passed |
| Go No Go | Create an effective slide presentation | Passed |
| Go No Go | Schedule the meeting | Passed |
| Go No Go | Respond to feedback | Passed |

## Overall Reviewer Note

🎉 🎉 Great progress on the project you’re very close to the finish line! 🎉 🎉

You’ve done an excellent job demonstrating end to end Product Manager skills, from planning and execution to communication and launch readiness. Across the project, you consistently showed structured thinking, sound judgment, and clear stakeholder communication.

- You created clear and well structured test plans, for non functional requirements with appropriate prioritization.
- You designed a thoughtful dogfood survey that balanced quantitative and qualitative insights, enabling meaningful internal feedback.
- You effectively prioritized competing scenarios, clearly stack ranking items and justifying decisions with rational, defensible reasoning.
- You identified the right stakeholders and chose appropriate communication methods for different scenarios.
- Your key messages were concise, actionable, and resolution focused, helping move discussions toward clear outcomes.
- You delivered a polished slide presentation, clearly outlining the product, value proposition, feature readiness, risks, and mitigation plans.
- Your launch recommendation was explicit, well reasoned, and easy for stakeholders to act on.
- You scheduled meetings thoughtfully, with the right invitees, strong context, and clear expectations.
- You responded to feedback clearly and professionally, showing openness to iteration and continuous improvement.
- **You need to prioritise your functional test cases.**

💡 As you continue to grow, keep sharpening your ability to tie data and readiness signals directly to decisions, and practice framing complex updates into even more executive friendly summaries. These habits will further strengthen your impact as a product leader.

If you have any questions or need clarification on any feedback, feel free to post them on the [Knowledge Section](https://knowledge.udacity.com/) our mentors and community are always here to support you.

Stay Udacious 😊

## Test Plan

### Write Test Cases for Functional Requirements — Requires Changes

#### Reviewer Note

**Well done,**

🟢 You’ve written clear, structured, and well-organized functional test cases that demonstrate a strong understanding of how product requirements translate into user-facing behavior. You’ve covered multiple core features, ensuring that the most important user journeys are validated in a way that is easy for QA, engineering, and stakeholders to follow.

🟢 Great job detailing each test case with ordered, step-by-step instructions and clearly defined expected behavior. The numbered steps (1, 2, 3, etc.) make execution straightforward, while the expected results remove ambiguity and set a clear pass/fail criterion exactly what effective functional testing requires.

#### Missing Requirement

🔴 Test case prioritization needs improvement. All test cases are marked as P1. In real product scenarios, this makes it difficult to focus on what is truly launch-blocking versus lower-risk functionality.

#### Suggestions

- Consider adding a short feature overview or user goal above each group of test cases to further clarify why that functionality is important.
- You could strengthen clarity by explicitly listing preconditions (e.g., user is logged in, feature flag enabled) where relevant.
- As products scale, maintaining a consistent template (Title, Priority, Steps, Expected Result) across all test cases will make reviews and execution even smoother.

#### Helpful Resources

- [How to Write Test Cases with Examples](https://www.guru99.com/test-case.html)

#### Submission Requirements

- At least 3 features are covered.
- There are at least 5 test cases for functional requirements.
- Test cases include detailed steps and expected behavior.
- Steps listed in ordered number format (1, 2, 3, etc).
- **Test cases are prioritized correctly — requires changes.**

### Write Test Cases for Non-functional Requirements — Passed

#### Reviewer Note

**Good job,**

🟢 You’ve written clear, structured, and well-organized non-functional test cases that show a solid grasp of quality attributes like performance, security, availability, and usability. Your focus on how the system should behave under real-world conditions (not just what it does) aligns with standard guidance on non-functional testing and sets your project up for reliable, scalable releases.

🟢 Great job providing at least three non-functional test cases with explicit priorities (P0/P1/P2). Using priority to reflect business impact and risk demonstrates mature product judgment and mirrors widely recommended, risk-aware approaches to test planning.

🟢 Your test cases are actionable and measurable (e.g., response-time thresholds, availability targets, security assertions), which makes pass/fail decisions unambiguous and aligns with best practices for writing NFRs and NFR tests.

#### Suggestions

- Where possible, add preconditions and metrics (e.g., “p95 API latency ≤ 300 ms under 1,000 concurrent users”) to strengthen reproducibility and engineering alignment.
- Keep prioritization risk-based: mark truly launch-blocking issues (e.g., auth security, payment performance) as P0, and defer lower-impact items to P1/P2 for efficient execution.
- Group NFR tests by category (performance, security, availability, usability) so stakeholders can quickly see coverage against the most common NFR types.

#### Helpful Resources

- [TestRail: Complete Guide to Non-Functional Testing](https://www.testrail.com/blog/non-functional-testing/)
- [BrowserStack: Non-Functional Requirements — Types & Examples](https://www.browserstack.com/guide/non-functional-requirements-examples)
- [TestRail: Test Case Prioritization — Techniques & Best Practices](https://www.testrail.com/blog/test-case-prioritization/)

#### Submission Requirements

- There are at least 3 test cases for non-functional requirements.
- Test cases are prioritized correctly.

## Dogfood Survey

### Create a Dogfood Survey — Passed

#### Reviewer Note

**Nice,**

🟢 You’ve created a comprehensive dogfood survey that meets all the core requirements and demonstrates strong product thinking. With 15+ well-structured questions, your survey gathers enough signal to meaningfully assess internal user feedback before launch exactly the goal of dogfooding.

🟢 Great job balancing high-level experience questions with deep dives into a specific feature. Including multiple questions about overall product experience helps identify broad usability or value issues, while focused feature questions allow teams to pinpoint actionable improvements.

🟢 It’s especially strong to see a mix of question types: yes/no, rating scale, and open-ended questions. This combination ensures you capture both quantitative trends (e.g., satisfaction scores) and qualitative insights (unexpected issues, suggestions, or edge cases). That blend is a best practice for internal feedback surveys.

🟢 Your questions are clear, logically ordered, and relevant to someone actively using the product, which increases response quality and reduces confusion. This shows good empathy for your survey participants and an understanding of how to design surveys that people actually complete.

#### Suggestions

- Consider grouping questions into short sections (e.g., Overall Experience, Feature Feedback, Reliability & Performance) to make longer surveys easier to scan and answer.
- For rating-scale questions, ensure the scale is labeled consistently (for example, 1 = Very dissatisfied, 5 = Very satisfied) to avoid misinterpretation.
- As you iterate, you can tag questions to specific product goals (adoption, retention, quality) to make analysis even more actionable.

#### Helpful Resources

- [Writing Good Survey Questions: 10 Best Practices - NN/G](https://www.nngroup.com/articles/survey-best-practices/)

#### Submission Requirements

- Survey contains at least 15 questions.
- At least 3 questions about the overall experience using the product.
- At least 3 questions about one specific feature.
- At least one yes/no question.
- At least one question with a rating scale.
- At least one open-ended question.

## Fire Drills & Prioritization

### Prioritize Effectively — Passed

#### Reviewer Note

**Good Attempt,**

🟢 You’ve demonstrated a strong ability to stack-rank scenarios clearly and logically, ensuring that the most urgent and high-impact items are surfaced and addressed first. This ordering makes your priorities immediately understandable and reflects real-world product and operational decision-making under time and resource constraints.

🟢 Great work rationalizing your prioritization. You don’t just state what comes first you explain why. By grounding your decisions in factors like user impact, business risk, urgency, and dependency, your prioritization feels intentional rather than subjective. This is exactly how effective prioritization supports alignment and buy-in across teams.

🟢 Your approach mirrors widely used product and delivery prioritization frameworks, showing that you understand how to move from competing inputs to a clear, defensible execution order. This makes it much easier for teams to act confidently and focus on what matters most.

#### Suggestions

- As you scale to larger backlogs, you may find it helpful to explicitly reference a framework (e.g., impact vs. effort, risk-based ranking) to keep prioritization consistent across scenarios.
- When presenting to senior stakeholders, consider summarizing your rationale in a single sentence per scenario to reinforce clarity and decision speed.

#### Helpful Resources

- [Product School – Product Prioritization Frameworks Explained](https://productschool.com/blog/product-fundamentals/ultimate-guide-product-prioritization)

#### Submission Requirements

- Scenarios are stack ranked so that the most urgent ones can be addressed first.
- All prioritization has been rationalized.

### Identify Correct Parties and Communicates Appropriately — Passed

#### Reviewer Note

**Awesome,**

🟢 You’ve clearly identified the right stakeholders for each scenario, demonstrating strong situational awareness and an understanding of how different roles contribute during launches, incidents, and decision-making moments. Mapping scenarios to owners such as engineering, support, leadership, or product reflects best practices in stakeholder identification and responsibility clarity.

🟢 Great job selecting appropriate communication methods based on urgency and complexity. Using real-time channels (e.g., Slack/war rooms) for high-severity issues and asynchronous methods (e.g., email or documents) for non-urgent updates aligns well with modern incident and stakeholder communication guidance. This ensures fast response without overloading teams.

🟢 Your approach shows thoughtful differentiation between informing, consulting, and collaborating. Executives receive concise status updates, operational teams get real-time coordination, and broader stakeholders are kept informed through structured updates an approach widely recommended for effective incident and stakeholder communication.

#### Suggestions

- Where possible, explicitly document a default channel per scenario (e.g., P0 outage → Slack war room + status page; non-urgent update → email) to make expectations even clearer.
- Consider adding a lightweight stakeholder communication matrix to show who is Responsible, Informed, or Consulted for each scenario this scales well as teams grow.

#### Helpful Resources

- [Atlassian – Incident Communication Best Practices](https://www.atlassian.com/incident-management/incident-communication)
- [Google SRE – Incident Management & Response Guide](https://sre.google/resources/practices-and-processes/incident-management-guide/)
- [Project Management Scope – Effective Stakeholder Communication Channels](https://projectmanagementscope.com/5-effective-channels-for-successful-stakeholder-communication/)
- [Simply Stakeholders – Stakeholder Communication Matrix](https://simplystakeholders.com/stakeholder-communication-matrix/)

#### Submission Requirements

- The correct person or persons have been identified for each scenario.
- The correct communication method has been identified for each scenario.

### Communicate with Concise, Actionable Key Messages — Passed

#### Reviewer Note

**Very well Implemented,**

🟢 You’ve done an excellent job crafting concise and focused key messages that get straight to the point. Each message avoids unnecessary detail while still providing enough context for stakeholders to quickly understand the situation an essential skill for effective product and incident communication.

🟢 Great work clearly outlining the specific actions required in each scenario. Your messages explicitly help teams see who needs to do what and by when, which removes ambiguity and helps teams move from discussion to execution without delay.

🟢 Most importantly, your key messages are resolution-oriented. Rather than simply describing the issue, they guide stakeholders toward closure by identifying the next step or decision needed. This ensures that open issues are not just communicated, but actively driven toward resolution—an approach recommended in both incident management and stakeholder communication best practices.

#### Suggestions

- As a next step, you might standardize your messages using a simple structure such as Context → Action → Outcome to maintain consistency across scenarios.
- When communicating to senior stakeholders, consider leading with the decision required to make key messages even more impactful.

#### Helpful Resources

- [Mind the Product – Communication Skills for Product Managers](https://www.mindtheproduct.com/category/communication/)
- [Harvard Business Review – How to Write Clear, Actionable Messages at Work](https://hbr.org/2016/11/how-to-write-email-with-military-precision)

#### Submission Requirements

- Key messages are concise.
- Key messages outline action needed/required.
- Key messages resolve the open issue in each scenario.

## Go No Go

### Launch Recommendation — Passed

#### Reviewer Note

**Nice,**

🟢 You’ve presented a clear and unambiguous launch recommendation right at the top of the slide, making it easy for stakeholders to immediately understand whether the product should launch or not. This executive-friendly structure aligns with best practices for decision-making presentations and launch reviews.

🟢 Great work backing your recommendation with three or more concise bullet points that explain the rationale. Each point directly supports the decision, helping the audience quickly assess readiness, risk, and confidence without needing additional context or discussion.

🟢 Your rationale is focused on relevant launch considerations such as product readiness, risk mitigation, and delivery confidence which demonstrates strong product judgment and an understanding of how launch decisions are made in real product organizations.

#### Suggestions

- You might consider ordering the rationale bullets from highest impact to lowest impact to further strengthen decision clarity.
- If the recommendation is “No-Go” or “Conditional Go,” briefly stating what conditions would change the decision can make the slide even more actionable.

#### Helpful Resources

- [Product School – Product Launch Go-to-Market Best Practices](https://productschool.com/blog/product-marketing/go-to-market-strategy)

#### Submission Requirements

- Clear recommendation to launch or not at the top of the slide.
- At least 3 bullet points explaining the rationale.

### Create an Effective Slide Presentation — Passed

#### Reviewer Note

**Awesome,**

🟢 You’ve created a clear and well-structured slide presentation that meets all the core requirements for an effective Go / No-Go and product readiness review. Including the product name prominently and opening with a concise description and value proposition immediately gives stakeholders the context they need to engage with the rest of the deck.

🟢 Great job highlighting three or more key features and dedicating individual slides to those specific features. Each slide is thoughtfully structured with a correct status label, making it easy to understand feature maturity at a glance an important best practice for executive and cross-functional audiences.

🟢 It’s especially strong to see production readiness metrics included (such as stability, performance, or adoption indicators). Backing feature status with measurable signals shows disciplined product thinking and helps stakeholders make more informed launch decisions.

🟢 You’ve also done a solid job identifying open issues and risks and, more importantly, outlining clear mitigation strategies. This moves the presentation beyond reporting into problem-solving, which is exactly what’s expected in launch readiness and leadership reviews.

#### Suggestions

- Consider standardizing feature slides with a consistent layout (Status → Metrics → Risks → Mitigation) to improve scan-ability.
- Where possible, quantify risk severity or likelihood to help stakeholders better assess trade-offs.
- A brief final slide summarizing overall launch recommendation (Go / No-Go / Conditional Go) could make decisions even clearer.

#### Submission Requirements

- Includes the name of the product.
- Includes a brief description with the value proposition.
- Lists at least 3 key features.
- At least 3 slides for specific features, including:
  - Correct status label.
  - At least 1 production readiness metric.
  - Correctly identify any open issues and risk.
  - Correctly describes ways to mitigate any risk.

### Schedule the Meeting — Passed

#### Reviewer Note

**Awesome,**

🟢 You’ve done a great job identifying the correct set of invitees for the meeting. The attendees clearly represent the right mix of decision-makers and cross-functional partners, ensuring that the meeting is set up for informed discussion and timely decisions.

🟢 Your meeting message is clear, concise, and purposeful. It quickly communicates why the meeting matters without unnecessary detail, making it easy for recipients to understand the context and be prepared.

🟢 Well done conveying excitement and momentum where the recommendation is to launch. The tone strikes a healthy balance between enthusiasm and professionalism, helping build alignment and energy around the milestone.

🟢 You’ve also included a brief but effective status overview, clearly explaining where things currently stand. Importantly, you call out key risks or considerations upfront, which sets the expectation for a productive, focused meeting rather than last-minute surprises.

#### Suggestions

- As a next step, you could add a short line clarifying the decision or outcome expected from the meeting to further sharpen focus.
- Listing any pre-reads or preparation items (if applicable) can make the discussion even more effective.

#### Submission Requirements

- Identifies the correct set of invitees.
- Concise message that:
  - Conveys excitement if the recommendation is to launch.
  - Includes a brief overview of where things are at.
  - Highlights any risk or key things to know before the meeting.

### Respond to Feedback — Passed

#### Reviewer Note

**Good job,**

🟢 You’ve responded to feedback with clear, structured bullet points, making it easy for reviewers and stakeholders to understand how the input was addressed.

🟢 Each bullet is direct and action-oriented, showing what changes were made or what decisions were taken rather than restating the feedback itself.

🟢 Your response demonstrates thoughtful consideration of the feedback, balancing alignment with stakeholder input while maintaining product judgment.

#### Submission Requirements

- At least 3 bullets in response.
