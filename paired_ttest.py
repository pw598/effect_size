
import streamlit as st
from pingouin import power_ttest2n

def run_paired_ttest():

	variable_menu = ['Power', 'Significance', 'Effect Size']
	variable = st.sidebar.selectbox('Estimation Statistic', variable_menu)

	if variable == 'Power':
		alpha = st.slider('Desired alpha (significance)?', 0.01, 1.00, 0.05)
		effect_size = st.slider('Desired effect size?', 0.0, 1.00, 0.80)
		sample_size_X = st.number_input('Desired X sample size?', value=20, step=1)
		sample_size_Y = st.number_input('Desired Y sample size?', value=20, step=1)
		alternative = st.selectbox('Type of Test', ('two-sided', 'greater', 'less'))

		power = power_ttest2n(alpha=alpha, nx=sample_size_X, ny=sample_size_Y, d=effect_size, alternative=alternative)
		st.write(variable + ' is: ' + str(round(power,4)))



	if variable == 'Significance':
		power = st.slider('Desired power?', 0.01, 1.00, 0.80)
		effect_size = st.slider('Desired effect size?', 0.0, 1.00, 0.80)
		sample_size_X = st.number_input('Desired X sample size?', value=20, step=1)
		sample_size_Y = st.number_input('Desired Y sample size?', value=20, step=1)
		alternative = st.selectbox('Type of Test', ('two-sided', 'greater', 'less'))

		signif = power_ttest2n(alpha=None, power=power, nx=sample_size_X, ny=sample_size_Y, d=effect_size, alternative=alternative)
		st.write(variable + ' is: ' + str(round(signif,4)))



	if variable == 'Effect Size':
		alpha = st.slider('Desired alpha (significance)?', 0.01, 1.00, 0.05)
		power = st.slider('Desired power?', 0.01, 1.00, 0.80)
		sample_size_X = st.number_input('Desired X sample size?', value=20, step=1)
		sample_size_Y = st.number_input('Desired Y sample size?', value=20, step=1)
		alternative = st.selectbox('Type of Test', ('two-sided', 'greater', 'less'))

		effect_size = power_ttest2n(power=power, alpha=alpha, nx=sample_size_X, ny=sample_size_Y, alternative=alternative)
		st.write(variable + ' is: ' + str(round(effect_size,4)))

