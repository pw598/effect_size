
import streamlit as st
from pingouin import power_chi2

def run_chi2_test():

	variable_menu = ['Power', 'Significance', 'Sample Size', 'Effect Size']
	variable = st.sidebar.selectbox('Estimation Statistic', variable_menu)

	if variable == 'Power':
		alpha = st.slider('Desired alpha (significance)?', 0.01, 1.00, 0.05)
		effect_size = st.slider('Desired effect size?', 0.0, 1.00, 0.80)
		dof = st.number_input('Desired degrees of freedom?', value=20, step=1)
		sample_size = st.number_input('Desired X sample size?', value=20, step=1)

		power = power_chi2(alpha=alpha, dof=dof, w=effect_size, n=sample_size)
		st.write(variable + ' is: ' + str(round(power,4)))



	if variable == 'Significance':
		power = st.slider('Desired power?', 0.01, 1.00, 0.80)
		effect_size = st.slider('Desired effect size?', 0.0, 1.00, 0.80)
		dof = st.number_input('Desired degrees of freedom?', value=20, step=1)
		sample_size = st.number_input('Desired X sample size?', value=20, step=1)

		alpha = power_chi2(power=power, dof=dof, w=effect_size, n=sample_size, alpha=None)
		st.write(variable + ' is: ' + str(round(alpha,4)))



	if variable == 'Sample Size':
		alpha = st.slider('Desired alpha (significance)?', 0.01, 1.00, 0.05)
		power = st.slider('Desired power?', 0.01, 1.00, 0.80)
		effect_size = st.slider('Desired effect size?', 0.0, 1.00, 0.80)
		dof = st.number_input('Desired degrees of freedom?', value=20, step=1)

		alpha = power_chi2(power=power, dof=dof, w=effect_size, alpha=alpha)
		st.write(variable + ' is: ' + str(round(alpha,0)))



	if variable == 'Effect Size':
		alpha = st.slider('Desired alpha (significance)?', 0.01, 1.00, 0.05)
		power = st.slider('Desired power?', 0.01, 1.00, 0.80)
		dof = st.number_input('Desired degrees of freedom?', value=20, step=1)
		sample_size = st.number_input('Desired X sample size?', value=20, step=1)

		effect_size = power_chi2(alpha=alpha, power=power, dof=dof, n=sample_size)
		st.write(variable + ' is: ' + str(round(effect_size,4)))
