
import streamlit as st

def run_about():

		st.title('Effect Size')
		st.write(r"""

It is common for statisticians to focus on the p-value and significance of a test, quantifying the likelihood of the result, 
while paying less attention to the magnitude of difference or relationship, also known as the effect. However, it is possible 
for a result to be significant but trivial, or important but nonsignificant.

Effect size refers to the size or magnitude of a result as it would be expected to occur in a population, and effect size 
methods are a collection of statistical tools used to calculate effect size.

Effect size can be reported in the original units of the variable, which can aid in domain-specific interpretation. It can 
also lack units, or have a standard scale, allowing it to be interpreted and compared regardless of application. A way to 
achieve the latter is with Cohen's d.

				""")

		st.header("Cohen's d")

		st.write("""		
The difference between groups is often referred to as the 'd' family of effect size methods, the most common among which is 
Cohen's d:
				""")
		st.write(r'$$d = \frac{ \mu_1 - \mu_2 }{ s }$$')
		st.write(r'$$s$$ is the pooled standard deviation of both variables, calculated as:')
		st.write(r'$$s = \sqrt{ \frac{ (n_1-1) \cdot s_1^2 + (n_2 - 1) \cdot s_2^2 }{ n_1 + n_2 - 2 } }$$')

		st.title('Statistical Power')
		st.write("""
The power of a hypothesis test is the probability of correctly rejecting the null hypothesis - i.e., the probability of 
detecting an effect if there is an effect to detect. It therefore only has relevance when the null hypothesis is false.
				""")

		st.write(r'$$Power = 1 - \text{Type II Error}$$')
		st.write(r'$$Pr(TP) = 1 - Pr(FN)$$')
		st.write("""
Statistical power is mainly affected by effect size and sample size. Low statistical power carries a large risk of committing 
Type II errors (false negatives), whereas the p-value indicates the probability of committing a type 1 error (false positive) 
for the significance level.
				""")