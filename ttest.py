
import streamlit as st
from pingouin import power_ttest

def run_ttest():

	variable_menu = ['Power', 'Significance', 'Sample Size', 'Effect Size']
	variable = st.sidebar.selectbox('Estimation Statistic', variable_menu)

	if variable == 'Power':
		alpha = st.slider('Desired alpha (significance)?', 0.01, 1.00, 0.05)
		effect_size = st.slider('Desired effect size?', 0.0, 1.00, 0.80)
		sample_size = st.number_input('Desired sample size?', value=20, step=1)
		alternative = st.selectbox('Type of Test', ('two-sided', 'greater', 'less'))

		power = power_ttest(alpha=alpha, d=effect_size, n=sample_size, alternative=alternative)
		st.write(variable + ' is: ' + str(round(power,4)))



	if variable == 'Significance':
		power = st.slider('Desired power?', 0.01, 1.00, 0.80)
		effect_size = st.slider('Desired effect size?', 0.0, 1.00, 0.80)
		sample_size = st.number_input('Desired sample size?', value=20, step=1)
		alternative = st.selectbox('Type of Test', ('two-sided', 'greater', 'less'))

		signif = power_ttest(power=power, n=sample_size, d=effect_size, alpha=None, alternative=alternative)
		st.write(variable + ' is: ' + str(round(signif,4)))



	if variable == 'Sample Size':
		alpha = st.slider('Desired alpha (significance)?', 0.01, 1.00, 0.05)
		power = st.slider('Desired power?', 0.0, 1.00, 0.80)
		effect_size = st.slider('Desired effect size?', 0.0, 1.00, 0.80)
		alternative = st.selectbox('Type of Test', ('two-sided', 'greater', 'less'))

		sample_size = power_ttest(power=power, alpha=alpha, d=effect_size, alternative=alternative)
		st.write(variable + ' is: ' + str(round(sample_size,0)))



	if variable == 'Effect Size':
		alpha = st.slider('Desired alpha (significance)?', 0.01, 1.00, 0.05)
		power = st.slider('Desired power?', 0.0, 1.00, 0.80)
		sample_size = st.number_input('Desired sample size?', value=20, step=1)
		alternative = st.selectbox('Type of Test', ('two-sided', 'greater', 'less'))

		effect_size = power_ttest(power=power, n=sample_size, alpha=alpha, alternative=alternative)
		st.write(variable + ' is: ' + str(round(effect_size,4)))




