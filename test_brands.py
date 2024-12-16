import allure
import requests

from modules.utils import generate_id, get_brand_fld


BASE_URL = 'https://api.practicesoftwaretesting.com/'


@allure.title('1 - Get list of all brands')
@allure.description('Get list of all brands and verify it is not empty.\n'
                    'Expected status code: 200')
@allure.link(url = 'https://api.practicesoftwaretesting.com/brands')
def test_get_all_brands():
    """
    Get list of all brands and verify it's not empty

    Expected status code: 200

    :return:
    """
    endpoint = 'brands'
    url = BASE_URL + endpoint
    response = requests.get(url)
    resp_json = response.json()
    print(resp_json)
    assert response.status_code == 200 and len(resp_json) > 0


@allure.title('2 - Add new brand')
@allure.description('Add new brand with randomly generated slug value and verify it was added.\n'
                    'Note: the added data gets deleted after a few minutes from the website database\n'
                    'Expected status code: 201')
@allure.link(url = 'https://api.practicesoftwaretesting.com/brands')
def test_add_new_brand():
    """
    Add new brand with randomly generated slug value and verify it was added.
    Note: the added data gets deleted after a few minutes from the website database

    Expected status code: 201

    :return:
    """
    endpoint = 'brands'
    url = BASE_URL + endpoint
    data = {
        'name': 'My Test Brand' + generate_id(),
        'slug': generate_id(),
    }
    response = requests.post(url, data = data)
    response_get_brands = requests.get(url)
    resp_json = response_get_brands.json()
    get_id = get_brand_fld(resp_json = resp_json,
                           data = data['name'],
                           key_fld = 'name',
                           src_fld = 'id')

    assert response.status_code == 201 and get_id != ''


@allure.title('3 - Partially update existing brand')
@allure.description('Partially update specific brand and verify it was updated.\n'
                    'Note: the added data gets deleted after a few minutes from the website database\n'
                    'Expected status code: 200')
@allure.link(url = 'https://api.practicesoftwaretesting.com/brands')
def test_part_update_brand():
    """
    Partially update specific brand and verify it was updated.
    Note: the added data gets deleted after a few minutes from the website database

    Expected status code: 200

    :return:
    """
    endpoint = 'brands'
    url = BASE_URL + endpoint
    name = 'My Test Brand4080'

    # get all brands list to retrieve the details of the specific one from it
    response_get_brands = requests.get(url)
    resp_json = response_get_brands.json()

    # get brand id to use it in the patch request
    get_id = get_brand_fld(resp_json = resp_json,
                           data = name,
                           key_fld = 'name',
                           src_fld = 'id')
    print('ID:', get_id)

    # get original brand slug value to verify it was changed as a result of the test
    get_slug = get_brand_fld(resp_json = resp_json,
                             data = get_id,
                             key_fld = 'id',
                             src_fld = 'slug')
    print('OLD SLUG:', get_slug)

    # generate new slug value
    data = {
        'slug': generate_id()
    }
    # sending request to update slug field value
    response = requests.patch(url + '/' + get_id, data = data)

    # fetching all brands again
    response_get_brands2 = requests.get(url)
    resp_json2 = response_get_brands2.json()

    # get new slug value
    get_new_slug = get_brand_fld(resp_json = resp_json2,
                                 data = get_id,
                                 key_fld = 'id',
                                 src_fld = 'slug')
    print('NEW SLUG:', get_new_slug)
    assert response.status_code == 200 and get_slug != get_new_slug


@allure.title('4 - Fully update existing brand')
@allure.description('Fully update specific brand and verify it was updated.\n'
                    'Note: the added data gets deleted after a few minutes from the website database\n'
                    'Expected status code: 200')
@allure.link(url = 'https://api.practicesoftwaretesting.com/brands')
def test_full_update_brand():
    """
    Fully update specific brand and verify it was updated.
    Note: the added data gets deleted after a few minutes from the website database

    Expected status code: 200

    :return:
    """
    endpoint = 'brands'
    url = BASE_URL + endpoint
    name = 'My Test Brand4080'
    new_name = 'My Test Brand ABC'

    # get all brands list to retrieve the details of the specific one from it
    response_get_brands = requests.get(url)
    resp_json = response_get_brands.json()

    # get brand id to use it in the patch request
    get_id = get_brand_fld(resp_json = resp_json,
                           data = name,
                           key_fld = 'name',
                           src_fld = 'id')
    print('ID:', get_id)

    # get original brand slug value to verify it was changed as a result of the test
    get_slug = get_brand_fld(resp_json = resp_json,
                             data = get_id,
                             key_fld = 'id',
                             src_fld = 'slug')
    print('OLD SLUG:', get_slug)

    # generate new name and slug values
    data = {
        'name': new_name,
        'slug': generate_id()
    }
    # sending request to update slug field value
    response = requests.put(url + '/' + get_id, data = data)

    # fetching all brands again
    response_get_brands2 = requests.get(url)
    resp_json2 = response_get_brands2.json()

    # get new slug value
    get_new_slug = get_brand_fld(resp_json = resp_json2,
                                 data = get_id,
                                 key_fld = 'id',
                                 src_fld = 'slug')

    get_new_name = get_brand_fld(resp_json = resp_json2,
                                 data = get_id,
                                 key_fld = 'id',
                                 src_fld = 'name')
    print('NEW SLUG:', get_new_slug)
    print('NEW NAME:', get_new_name)
    assert response.status_code == 200 and get_slug != get_new_slug and get_new_name != name


@allure.title('5 - Delete specific brand')
@allure.description('Delete specific brand.\n'
                    'This is action is not allowed for users without the Admin role as stated on the website.\n'
                    'Note: the added data gets deleted after a few minutes from the website database.\n'
                    'Expected status code: 401.\n'
                    'Expected message: Unauthorized')
@allure.link(url = 'https://api.practicesoftwaretesting.com/brands')
def test_delete_brand():
    """
    Delete specific brand.
    This is action is not allowed for users without the Admin role as stated on the website
    Note: the added data gets deleted after a few minutes from the website database

    Expected status code: 401
    Expected message: Unauthorized

    :return:
    """
    endpoint = 'brands'
    url = BASE_URL + endpoint
    name = 'My Test Brand ABC'

    # get all brands list to retrieve the details of the specific one from it
    response_get_brands = requests.get(url)
    resp_json = response_get_brands.json()

    # get brand id to use it in the delete request
    get_id = get_brand_fld(resp_json = resp_json,
                           data = name,
                           key_fld = 'name',
                           src_fld = 'id')
    response = requests.delete(url + '/' + get_id)
    assert response.status_code == 401 and response.json()['message'] == 'Unauthorized'

