from multiprocessing.pool import AsyncResult
from tracemalloc import stop
import urllib3
import time

import swagger_client

urllib3.disable_warnings()


def current_milli_time():
    return round(time.time() * 1000)


def monitor_thread_groups(current_thread_groups):
    print('monitor_thread_groups - START')
    while True:
        all_groups_done = True
        
        for thread_group in current_thread_groups:
            if thread_group['done'] is True:
                continue
            if thread_group['done'] is False:
                all_groups_done = False

            num_done = 0
            all_done = True

            for idx, thread in enumerate(thread_group['threads']):
                is_ready = thread.ready()
                if not is_ready:
                    all_done = False
                
                if thread.ready():
                    # r = thread.get()
                    # print(r)
                    num_done += 1

            # time_ecip = round((current_milli_time() - thread_group['start_milli_time']) / 1000)
            # rate_per_sec = 0
            # if num_done != 0:
            #     rate_per_sec = num_done / time_ecip

            # print('{}\t{}\t{}\t{}'.format(thread_group['group_name'], num_done, time_ecip, rate_per_sec))
            
            print('{}\t{}\t{}'.format(current_milli_time(), thread_group['group_name'], num_done))

            if all_done:
                print('GROUP: {} IS DONE'.format(thread_group['group_name']))
                thread_group['done'] = True
        
        if all_groups_done:
            print('ALL GROUPS DONE')
            break

        time.sleep(1)

    print('monitor_thread_groups - END')


# create an instance of the API class
config = swagger_client.Configuration()
config.host = 'https://localhost:8443/mobirest'
config.verify_ssl = False
worker_count = 1 # Too many threads makes mobi very slow
api_client_instance = swagger_client.ApiClient(config, worker_count=worker_count)
api_client_instance_1 = swagger_client.ApiClient(config, worker_count=worker_count)
session_api = swagger_client.SessionApi(api_client_instance)
user_api = swagger_client.UsersApi(api_client_instance)
group_api = swagger_client.GroupsApi(api_client_instance_1)

# Data
def gen_user_objects():
    for user_id in range(1000, 9000):
        yield {'username': 'user{}'.format(user_id), 'password': 'password'}

def gen_group_objects():
    for group_id in range(1000, 9000):
        yield {'title': 'group{}'.format(group_id)}

user_objects_gen = (gen_user_objects())
group_objects_gen = (gen_group_objects())

thread_groups = [
    {'group_name': 'done', 'done': True, 'threads':[]}
]

try:
    data = session_api.login('admin', 'admin')
    token_cookie = data[2]['Set-Cookie']
    api_client_instance.cookie = token_cookie

    user_objects_group = {'group_name': 'user_objects_threads', 'done': False, 'threads':[], 'start_milli_time': current_milli_time()}
    group_objects_group = {'group_name': 'group_objects_threads', 'done': False, 'threads':[], 'start_milli_time': current_milli_time()}
    thread_groups.append(user_objects_group)
    thread_groups.append(group_objects_group)

    while True:
        more_group_object = True
        try:
            group_object = next(group_objects_gen)
            response_thread: AsyncResult = group_api.create_group_with_http_info(
                title=group_object['title'], 
                _return_http_data_only=False, 
                async_req=True
            )
            group_objects_group['threads'].append(response_thread)
        except StopIteration as e:
            more_group_object = False


        more_user_object = True
        try:
            user_object = next(user_objects_gen)
            create_user_response_thread: AsyncResult = user_api.create_user_with_http_info(
                username=user_object['username'], 
                password=user_object['password'], 
                _return_http_data_only=False, 
                async_req=True
            )
            user_objects_group['threads'].append(create_user_response_thread)
        except StopIteration as e:
            more_user_object = False

        if not more_user_object and not more_group_object:
            break

    print('==thread_groups==')
    for thread_group in thread_groups:
        print('\t{}\t{}\t{}'.format(thread_group['group_name'], thread_group['done'], len(thread_group['threads'])))

    monitor_thread_groups(thread_groups)
# except Exception as e:
#     print('===== Exception was raised =====')
#     print(e)
finally:
    print('==close==')
    # del api_client_instance
    api_client_instance.pool.close()
    api_client_instance.pool.join()

    api_client_instance_1.pool.close()
    api_client_instance_1.pool.join()
