import configparser

config = configparser.ConfigParser()
config.read('./1_config.conf')

print('\n ===== Dev configs =====')
ENV_VAR = 'DEV'
param1 = config.get(ENV_VAR, "param1")
param2 = config.get(ENV_VAR, "param2")
print('Value of param1 is = ', param1)
print('Value of param2 is = ', param2)

print('\n ===== QA configs =====')
ENV_VAR = 'QA'
param1 = config.get(ENV_VAR, "param1")
param2 = config.get(ENV_VAR, "param2")
print('Value of param1 is = ', param1)
print('Value of param2 is = ', param2)

print('\n===== PROD configs =====')
ENV_VAR = 'PROD'
param1 = config.get(ENV_VAR, "param1")
param2 = config.get(ENV_VAR, "param2")
print('Value of param1 is = ', param1)
print('Value of param2 is = ', param2)