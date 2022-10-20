import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re
import plotly.express as px

df = pd.read_csv('GB.csv', encoding='utf-8')

df['hit_date'] = pd.to_datetime(df['hit_date'])
df = df.astype({'claim': bool, '60sec': bool, 'scroll_90': bool, 'has_vk_id': bool, 'has_ok_id': bool})
df['gender'] = df['gender'].replace({1: 'female', 0: 'male', -1: 'not identification'})
df['age'] = df['age'].replace({-1: 'nan'})


def group(age):
    if age == 'nan':
        return 'group not identification'
    if age < 25:
        return 'group < 25'
    if 25 < age < 40:
        return 'group 25 - 40'
    if age > 40:
        return 'group > 40'


df['group_age'] = df['age'].apply(group)
df['group_age'] = df['group_age'].fillna('group not identification')
group_age = df['group_age'].value_counts()

# plt.pie(group_age, labels=group_age.index, autopct='%.0f%%')
# plt.title('Количество посещений в возрастных группах в процентах от общего количества')


df['Day_week'] = df['hit_date'].dt.dayofweek
df['Day_week'] = df['Day_week'].replace({2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday'})
group_dayofweek = df['Day_week'].value_counts()

# plt.pie(group_dayofweek, labels=group_dayofweek.index, autopct='%.0f%%')
# plt.title('Количество посещений в разные дни недели в процентах от общего количества')


# sns.heatmap(df.corr(), annot=True, vmin=-1, vmax=1)
# plt.title('Тепловая карта корреляции признаков')


df_group_claim = pd.DataFrame(df['group_age'])
df_group_claim['gender'] = df['gender']
df_group_claim['claim'] = df['claim']

group_by_claim = df_group_claim.groupby('claim').value_counts()

acccepted_application_False_by_age_and_gender = pd.DataFrame({'value_claim': [i for i in group_by_claim[:9]],
                                                              'group_age': ['group < 25', 'group 25-40',
                                                                            'group 25-40', 'group > 40', 'group < 25',
                                                                            'group < 25', 'group > 40',
                                                                            'group not identification',
                                                                            'group not identification'
                                                                            ],
                                                              'gender': ['not identification', 'male', 'female',
                                                                         'female', 'male', 'female', 'male', 'male',
                                                                         'female']})
acccepted_application_True_by_age_and_gender = pd.DataFrame({'value_claim': [i for i in group_by_claim[9:]],
                                                             'group_age': ['group < 25', 'group < 25', 'group 25-40',
                                                                           'group 25-40', 'group < 25', 'group > 40',
                                                                           'group > 40',
                                                                           'group not identification',
                                                                           'group not identification'
                                                                           ],
                                                             'gender': ['not identification', 'male', 'male',
                                                                        'female', 'female', 'female', 'male', 'female',
                                                                        'male']})

# plt.figure(figsize=(16, 8))
# ax = sns.barplot(data=acccepted_application_True_by_age_and_gender, x='group_age', y='value_claim', hue='gender')
# for i in ax.containers:
#     ax.bar_label(i, )
# plt.title('Количество принятых заявок в зависимости от возраста и пола')


# ax = sns.barplot(data=acccepted_application_False_by_age_and_gender, x='group_age', y='value_claim', hue='gender')
# for i in ax.containers:
#     ax.bar_label(i, )
# plt.title('Количество принятых заявок в зависимости от возраста и пола')


accepted_applications = df.groupby(['claim'])['group_age'].value_counts()
accepted_applications_False_by_group_age = pd.Series([i for i in accepted_applications[:4]],
                                                     index=['group < 25', 'group 25-40', 'group > 40',
                                                            'group not identification'])
accepted_applications_True_by_group_age = pd.Series([i for i in accepted_applications[4:]],
                                                    index=['group < 25', 'group 25-40', 'group > 40',
                                                           'group not identification'])


# plt.pie(accepted_applications_True_by_group_age, labels=accepted_applications_True_by_group_age.index, autopct='%0.f%%')
# plt.title('Количество принятых заявок по возрастным группам')


# plt.pie(accepted_applications_False_by_group_age, labels=accepted_applications_False_by_group_age.index,
#         autopct='%0.f%%')
# plt.title('Количество не принятых заявок по возрастным группам')

# accepted_applications_by_dayofweek = df.groupby(['claim'])['Day_week'].value_counts()
# accepted_applications_by_dayofweek_False = pd.Series([i for i in accepted_applications_by_dayofweek[:4]],
#                                                      index=['Thursday', 'Wednesday', 'Saturday', 'Friday'])
# accepted_applications_by_dayofweek_True = pd.Series([i for i in accepted_applications_by_dayofweek[4:]],
#                                                     index=['Thursday', 'Wednesday', 'Saturday', 'Friday'])

# plt.pie(accepted_applications_by_dayofweek_False, labels=accepted_applications_by_dayofweek_False.index, autopct='%0.f%%')
# plt.title('Количество непринятых заявок по дням недели в процентном соотношении')
#
# plt.pie(accepted_applications_by_dayofweek_True, labels=accepted_applications_by_dayofweek_True.index, autopct='%0.f%%')
# plt.title('Количество принятых заявок по дням недели в процентном соотношении')


def group_sear(string):
    group_1 = ['posts', 'confirmation', 'black', 'ru/csharp', 'company', 'about', 'feedback', 'find', 'search', 'dao',
               'promo', 'referrals', 'geek', 'live']
    group_2 = ['university', 'wizard', 'courses', 'leader', 'why_go', 'education', 'event', 'professions', 'dev_team',
               'partners', 'work', 'team']
    group_3 = ['sferum', 'edufree', 'test', 'login', 'profile', 'password', 'notices', 'cart', 'register', 'account',
               'masterclass']
    group_4 = ['chat', 'calendar', '/a/', 'career', 'redeem', 'order', 'webinar', 'work']

    for group_search_2 in group_2:
        if re.search(group_search_2, string):
            return 'Interest'
    for group_search_3 in group_3:
        if re.search(group_search_3, string):
            return 'Desire'
    for group_search_4 in group_4:
        if re.search(group_search_4, string):
            return 'Action'
    for group_search_1 in group_1:
        if re.search(group_search_1, string):
            return 'Visit'
    if len(string) == 14:
        return 'Visit'


df['group_of_sales'] = df['url'].apply(group_sear)

data = {'number': [22, 43, 25, 7],
        'stage': ['Visit', 'Interest', 'Desire', 'Action']}
fig = px.funnel(data, x='number', y='stage')
fig.show()

print()
