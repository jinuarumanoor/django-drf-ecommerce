import json
import pytest
import factory
from Drfecommerce.tests.factories import CategoryFactory,BrandFactory,ProductFactory
pytestmark=pytest.mark.django_db


class TestCategoryEndPoints:
    endpoint='/api/category/'

    def test_category_get(self,category_factory,api_client):
        #Arrange
        CategoryFactory.create_batch(4)
        #act
        response=api_client().get(self.endpoint)
        #assert
        assert response.status_code == 200 
        print(json.loads(response.content))
        assert len(json.loads(response.content)) == 4
     
class TestBrandEndpoints:
    endpoint='/api/brand/'

    def test_brand_get(self,product_factory,api_client):
        #Arrange
        BrandFactory.create_batch(4)
        #act
        response=api_client().get(self.endpoint)
        #assert
        assert response.status_code == 200 
        print(json.loads(response.content))
        assert len(json.loads(response.content)) == 4

class TestProductEndpoints:
    endpoint='/api/product/'

    def test_product_get(self,brand_factory,api_client):
        #Arrange
        ProductFactory.create_batch(4)
        #act
        response=api_client().get(self.endpoint)
        #assert
        assert response.status_code == 200 
        print(json.loads(response.content))
        assert len(json.loads(response.content)) == 4
    