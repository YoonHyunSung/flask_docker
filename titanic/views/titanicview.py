from titanic.models.dataset import Dataset
from titanic.models.titanic_service import TitanicService


class TitanicView(object):
    dataset = Dataset()
    service = TitanicService()

    def modeling(self):
        this = self.service.preprocessing()
        return this
        #service = self.service
        #this = self.preprocessing(train,test)
        #print(f'The Type of This is {type(this.train)}')
        #print(f'The head of Train is \n {this.train.head(2)}')
        #print(f'The head of Test is \n {this.test.head(2)}')

    def preprocessing(self) -> object:
        service = self.service
        this = self.dataset
        this.train = service.new_model("train")
        this.test = service.new_model("test")
        return this
#if __name__ == '__main__':
