class Car(object):
    name='Toyota'
    model='corolla'
    num_of_doors=4
    speed=0


    def __init__( self, name='Toyota', model='corolla', car_type='car', num_of_wheels=4, num_of_doors=4):
        self.name=name
        self.model=model
        self.car_type=car_type
        self.speed=0
        num_of_wheels=4

        if self.name == "Benz" or self.name == "mercedez":
            self.num_of_doors = 2
        else:
            self.num_of_doors = 4

        if (self.car_type == 'canta'):
            self.num_of_wheels = 8
        else:
            self.num_of_wheels = 4


    # is_saloon Car
    def is_porshe(self):
        if self.car_type != 'canta':
            return True
        else:
            return False


    # Car Speed
    def drive(self, accelerate):
        if (self.car_type == 'canta'):
            self.speed = int(accelerate * 11)
            return self
        else:
            if(accelerate !=0):
                self.speed = 10 ** accelerate
            else:
                self.speed = 10 * accelerate
            return self