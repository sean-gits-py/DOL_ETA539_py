import pandas as pd
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

csv_url = 'https://oui.doleta.gov/unemploy/csv/ar539.csv'
df = pd.read_csv(csv_url)

df.columns = ['state', 'report_date', 'wk_nbr', 'claim_date', 'initial_claims', 'fed_init_claims', 'fmr_servicemembers_init_claims', 'wrkshare_init_claims', 'wrkshare_equiv_init_claims', 'contd_wks_claims', 'fed_contd_wks_claims', 'fmr_serv_memb_contd_wks_claims', 'wrkshare_contd_wks_claims', 'wrkshare_equiv_contd_wks_claims', 'extd_bnft_prog_contd_wks_claims', 'extd_bnft_addl_bnft_prog_contd_wks_claims', 'state_addl_bnft_prog_contd_wks_claims_a', 'state_addl_bnft_prog_contd_wks_claims_b', 'avg_adj_total_contd_wks_claims', 'qtr_avg_monthly_covered_employment', 'rate_of_insured unemployment', 'Avg_rate_of_insured_unemployment_last_two_yrs', 'curr_rate_prct_avg_rate_last_two_yrs', 'state_extd_bnft_period_beg_end', 'status_chg_date', 'curdate', 'prior_wk_pub', 'prior_wk']

df.head()

#
