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
sb.boxplot(x='SITE', y='TEXT_WORD_COUNT', data=data[data['TEXT_WORD_COUNT'] < 5000], showfliers=False)  # Hide original outliers
sb.swarmplot(x='SITE', y='TEXT_WORD_COUNT', data=data[data['TEXT_WORD_COUNT'] < 5000], hue='SITE', size=1, alpha=0.4)
plt.title('Boxplot of Word Count in Text')
plt.xlabel('Category')
plt.ylabel('Number of Words')
mean_values = data.groupby('SITE')['TEXT_WORD_COUNT'].mean()
for i, mean in enumerate(mean_values):
    plt.text(i, mean, f'{mean:.2f}', color='black', ha="center", va="center", fontweight="bold")
plt.savefig('plots/word_count_text.pdf')
plt.show()
# #e
# data['Datetime'] = pd.to_datetime(data['DATE'])
# data['YearMonth'] = data['Datetime'].dt.to_period('M')
# monthly_avg = data.groupby(['SITE', 'YearMonth']).size().reset_index(name='AverageRows')
# monthly_avg['YearMonth'] = monthly_avg['YearMonth'].dt.to_timestamp()
# sb.lineplot(x='YearMonth', y='AverageRows', hue='SITE', data=monthly_avg)
# plt.title('Average Number of Rows per Month by SITE')
# plt.xlabel('Month')
# plt.ylabel('Average Number of Rows')
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.savefig('plots/average_data_per_month_per_site.pdf')
# plt.show()