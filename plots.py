import seaborn as sb
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


data = pd.read_excel("data/results.xlsx")

print(data)

'''
    Figure 2:
'''
# sb.countplot(x='SITE', data=data)
# plt.title('Number of texts by site')
# plt.xlabel('Site')
# plt.ylabel('Count')
# plt.savefig('plots/counts.pdf')
# plt.show()

#a
# sb.boxplot(x='SITE', y='TEXT_CHAR_COUNT', data=data, showfliers=False)  # Hide original outliers
# sb.swarmplot(x='SITE', y='TEXT_CHAR_COUNT', data=data, hue='SITE', size=1, alpha=0.4)
# plt.title('Boxplot of Character Count by Category')
# plt.xlabel('Category')
# plt.ylabel('Number of Characters')
# mean_values = data.groupby('SITE')['TEXT_CHAR_COUNT'].mean()
# for i, mean in enumerate(mean_values):
#     plt.text(i, mean, f'{mean:.2f}', color='black', ha="center", va="center", fontweight="bold")
# plt.savefig('plots/text_char_count.pdf')
# plt.show()
#b
# sb.boxplot(x='SITE', y='HEADLINE_CHAR_COUNT', data=data[data['HEADLINE_CHAR_COUNT'] < 1000], showfliers=False)  # Hide original outliers
# sb.swarmplot(x='SITE', y='HEADLINE_CHAR_COUNT', data=data[data['HEADLINE_CHAR_COUNT'] < 1000], hue='SITE', size=1, alpha=0.4)
# plt.title('Boxplot of Character Count in headlines')
# plt.xlabel('Category')
# plt.ylabel('Number of Characters')
# mean_values = data.groupby('SITE')['HEADLINE_CHAR_COUNT'].mean()
# for i, mean in enumerate(mean_values):
#     plt.text(i, mean, f'{mean:.2f}', color='black', ha="center", va="center", fontweight="bold")
# plt.savefig('plots/headline_char_count.pdf')
# plt.show()
#
# #c
# sb.boxplot(x='SITE', y='HEADLINE_WORD_COUNT', data=data[data['HEADLINE_CHAR_COUNT'] < 300], showfliers=False)  # Hide original outliers
# sb.swarmplot(x='SITE', y='HEADLINE_WORD_COUNT', data=data[data['HEADLINE_CHAR_COUNT'] < 300], hue='SITE', size=1, alpha=0.4)
# plt.title('Boxplot of Word Count in Headline')
# plt.xlabel('Category')
# plt.ylabel('Number of Words')
# mean_values = data.groupby('SITE')['HEADLINE_WORD_COUNT'].mean()
# for i, mean in enumerate(mean_values):
#     plt.text(i, mean, f'{mean:.2f}', color='black', ha="center", va="center", fontweight="bold")
# plt.savefig('plots/word_count_headline.pdf')
# plt.show()
# # d
# sb.boxplot(x='SITE', y='TEXT_WORD_COUNT', data=data[data['TEXT_WORD_COUNT'] < 5000], showfliers=False)  # Hide original outliers
# sb.swarmplot(x='SITE', y='TEXT_WORD_COUNT', data=data[data['TEXT_WORD_COUNT'] < 5000], hue='SITE', size=1, alpha=0.4)
# plt.title('Boxplot of Word Count in Text')
# plt.xlabel('Category')
# plt.ylabel('Number of Words')
# mean_values = data.groupby('SITE')['TEXT_WORD_COUNT'].mean()
# for i, mean in enumerate(mean_values):
#     plt.text(i, mean, f'{mean:.2f}', color='black', ha="center", va="center", fontweight="bold")
# plt.savefig('plots/word_count_text.pdf')
# plt.show()
# #e
# data['Datetime'] = pd.to_datetime(data['DATE'])
# data['YearMonth'] = data['Datetime'].dt.to_period('M')
# monthly_avg = data.groupby(['SITE', 'YearMonth']).size().reset_index(name='AverageRows')
# monthly_avg['YearMonth'] = monthly_avg['YearMonth'].dt.to_timestamp()
# plt.figure(figsize=(8, 5))
# sb.lineplot(x='YearMonth', y='AverageRows', hue='SITE', data=monthly_avg)
# plt.title('Average Number of Rows per Month by SITE')
# plt.xlabel('Month')
# plt.ylabel('Average Number of Rows')
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.savefig('plots/average_data_per_month_per_site.pdf')
# plt.show()

import matplotlib.dates as mdates
'''
    Figure 4
'''
# data['Datetime'] = pd.to_datetime(data['DATE'])
# data['YearMonth'] = data['Datetime'].dt.to_period('M')
# monthly_avg = data.groupby(['SITE', 'YearMonth']).mean().reset_index()
# monthly_avg['YearMonth'] = monthly_avg['YearMonth'].dt.to_timestamp()
# sites = monthly_avg['SITE'].unique()
# n_sites = len(sites)
# ncols = 1  # Number of columns in the subplot grid
# nrows = 4 # Calculate number of rows needed
#
# fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=(12, 8), sharex=True, sharey=True)
# axes = axes.flatten()
# for i, site in enumerate(sites):
#     ax = axes[i]
#     site_data = monthly_avg[monthly_avg['SITE'] == site]
#
#     sb.lineplot(x='YearMonth', y='TEXT_decision_social_prob', data=site_data, ax=ax, linewidth=2,
#                   label='TEXT_prob', color='#304269', marker='o')
#     sb.lineplot(x='YearMonth', y='HEADLINE_decision_social_prob', data=site_data, ax=ax, linewidth=2,
#                  label='HEADLINE_prob', color='#F26101',marker='o')
#     ax.axhline(y=0, color='red', linestyle='--', alpha=0.5)
#     ax.set_title(f'SITE: {site}')
#     ax.set_xlabel('Date')
#     ax.set_ylabel('Score')
#     ax.legend(title='Score Type')
#
# for j in range(len(sites), len(axes)):
#     fig.delaxes(axes[j])
# plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
# plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
# plt.xticks(rotation=90, fontsize=8)
# plt.tight_layout()
# plt.savefig('plots/figure4_part.pdf')
# plt.show()
#
#
data = pd.read_excel("data/COVID-data.xlsx")
data['Datetime'] = pd.to_datetime(data['date'])
data['YearMonth'] = data['Datetime'].dt.to_period('M')
monthly_avg = data.groupby(['location', 'YearMonth']).mean().reset_index()
monthly_avg['YearMonth'] = monthly_avg['YearMonth'].dt.to_timestamp()

plt.Figure((8,5))
sb.lineplot(x='YearMonth', y='new_deaths', hue='location', data=monthly_avg, style=False,
            linewidth=2, markers='o', dashes=[(None, None)], palette='Set1')
plt.title('Comparison of Scores Over Time by SITE')
plt.xlabel('Date')
plt.yscale('log')
# Formatting x-axis to show both month and year
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
plt.xticks(rotation=90, fontsize=8)
plt.tight_layout()
plt.savefig('plots/figure4_part3.pdf')
plt.show()
