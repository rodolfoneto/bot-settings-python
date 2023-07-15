import simplejson
from pathlib import Path

def read_directory():
    for child in Path('C:\\Users\\User\\Desktop\\bot\\LordsBot-Release 4.9\\config').iterdir():
        if child.is_dir() and child.name != 'global':
            if Path('C:\\Users\\User\\Desktop\\bot\\LordsBot-Release 4.9\\config\\'+child.name+'\\settings.json').exists():
                f_settings = open('C:\\Users\\User\\Desktop\\bot\\LordsBot-Release 4.9\\'+child.name+'\\acc.json', 'r')
                print(f_settings.readlines())
# read_directory()

def get_accounts_directory():
    list_accounts = []
    for child in Path('C:\\Users\\User\\Desktop\\bot\\LordsBot-Release 4.9\\config').iterdir():
        if child.is_dir() and child.name != 'global':
            list_accounts.append(child.name)
    return list_accounts
# print(get_accounts_directory())

def get_settings_txt_by_account_id(account_id):
    path = 'C:\\Users\\User\\Desktop\\bot\\LordsBot-Release 4.9\\config\\' + account_id
    if Path(path).exists() and Path(path).is_dir():
        path_file = path + '/acc.json'
        if Path(path_file).exists() and Path(path_file).is_file():
            file = open(path_file, 'r')
            content_file = file.readlines()
            file.close()
            # print(simplejson.load(content_file))
            return content_file
# get_settings_txt_by_account_id(get_accounts_directory()[0])

def get_settings_like_object(settings_txt):
    settings = simplejson.loads(settings_txt)
    return settings
# get_settings_like_object(get_settings_txt_by_account_id(get_accounts_directory()[0]))

def get_object_by_id(account_id):
    aa = get_settings_txt_by_account_id(account_id)
    return get_settings_like_object(aa)

# def write_file(path, content):
#     path = 'C:\\Users\\User\\Desktop\\bot\\LordsBot-Release 4.9\\config\\' + path + '\\acc.json'
#     if Path(path).exists():
#         f_settings = open(path, 'w')
#         f_settings.write(content)
#         f_settings.close
#         return True
        # print('wrote in file')
# write_file('1625104223', "{nossa:'Senhora'}")
