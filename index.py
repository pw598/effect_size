
import streamlit as st
from about import run_about
from ttest import run_ttest
from paired_ttest import run_paired_ttest
from chi_sq_test import run_chi2_test
from corr_test import run_corr_test


def main():
	test_menu = ['About', 'T-Test', 'Paired T-Test', 'Chi-Square Test', 'Correlation Test']
	test = st.sidebar.selectbox('Menu', test_menu)

	if test != 'About':
		st.title(test + ' Power with Pingouin')
	else:
		st.title('Effect Size and Statistical Power')

	if test == 'T-Test':
		run_ttest()
	elif test == 'Paired T-Test':
		run_paired_ttest()
	elif test == 'Chi-Square Test':
		run_chi2_test()
	elif test == 'Correlation Test':
		run_corr_test()
	else:
		run_about()


if __name__ == '__main__':
	main() 




