
import streamlit as st
from pingouin import power_corr

def run_corr_test():

	variable_menu = ['Power', 'Significance', 'Sample Size', 'Correlation Coefficient']
	variable = st.sidebar.selectbox('Estimation Statistic', variable_menu)

	if variable == 'Power':
		alpha = st.slider('Desired power?', 0.01, 1.00, 0.05)
		r = st.slider('Hypothetical correlation coefficient?', 0.0, 1.00, 0.40)
		sample_size = st.number_input('Desired sample size?', value=20, step=1)
		alternative = st.selectbox('Type of Test', ('two-sided', 'greater', 'less'))

		power = power_corr(alpha=alpha, r=r, n=sample_size, alternative=alternative)
		st.write(variable + ' is: ' + str(round(power,4)))



	if variable == 'Significance':
		power = st.slider('Desired alpha (significance)?', 0.0, 1.00, 0.80)
		r = st.slider('Hypothetical correlation coefficient?', 0.0, 1.00, 0.40)
		sample_size = st.number_input('Desired sample size?', value=20, step=1)
		alternative = st.selectbox('Type of Test', ('two-sided', 'greater', 'less'))

		alpha = power_corr(power=power, alpha=None, r=r, n=sample_size, alternative=alternative)
		st.write(variable + ' is: ' + str(round(alpha,4)))



	if variable == 'Sample Size':
		alpha = st.slider('Desired alpha (significance)?', 0.01, 1.00, 0.05)
		power = st.slider('Desired power?', 0.0, 1.00, 0.80)
		r = st.slider('Hypothetical correlation coefficient?', 0.0, 1.00, 0.40)
		alternative = st.selectbox('Type of Test', ('two-sided', 'greater', 'less'))

		sample_size = power_corr(power=power, alpha=alpha, r=r, alternative=alternative)
		st.write(variable + ' is: ' + str(round(sample_size,0)))



	if variable == 'Correlation Coefficient':
		alpha = st.slider('Desired alpha (significance)?', 0.01, 1.00, 0.05)
		power = st.slider('Desired power?', 0.0, 1.00, 0.80)
		sample_size = st.number_input('Desired sample size?', value=20, step=1)
		alternative = st.selectbox('Type of Test', ('two-sided', 'greater', 'less'))

		effect_size = power_corr(power=power, alpha=alpha, n=sample_size, alternative=alternative)
		st.write(variable + ' is: ' + str(round(effect_size,4)))




