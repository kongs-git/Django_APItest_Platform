from django.test import TestCase

# Create your tests here.


@login_required
def diffCaseResponse(request, test_record_id):
    test_record_data = models.TestCaseExecuteRecord.objects.get(id=test_record_id)
    print("test_record_data: {}".format(test_record_data))
    present_response = test_record_data.response_data
    if present_response:
        print("present_response in db: {}".format(present_response))
        present_response = json.dumps(json.loads(present_response), sort_keys=True, indent=4,
                                      ensure_ascii=False)  # 中文字符不转ascii编码
        print("present_response: {}".format(present_response))
    last_time_execute_response = test_record_data.last_time_response_data
    if last_time_execute_response:
        print("last_time_execute_response in db".format(last_time_execute_response))
        last_time_execute_response = json.dumps(json.loads(last_time_execute_response), sort_keys=True, indent=4,
                                                ensure_ascii=False)
        print("last_time_execute_response after json.dumps "''": {}".format(last_time_execute_response))
    print("last_time_execute_response: {}".format(last_time_execute_response))
    return render(request, 'diffResponse.html', locals())