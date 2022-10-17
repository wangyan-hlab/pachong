import os 

dir_name_list = ['cat', 'deer', 'dog', 'hedgehog', 'horse', 
                 'leopard', 'lion', 'rabbit', 'tiger', 'wolf']

for dir_name in dir_name_list:
    n = 0
    img_dir = f"images/animals/{dir_name}"

    train_dir = f'data/animals/train/{dir_name}'
    if not os.path.exists(train_dir):
        os.makedirs(train_dir)
    val_dir = f'data/animals/val/{dir_name}'
    if not os.path.exists(val_dir):
        os.makedirs(val_dir)

    while n < 100:
        with open(os.path.join(img_dir, f'{n:06d}.jpg'), 'rb') as img:
            image_data = img.read()
        with open(os.path.join(f'{train_dir}/{n:06d}.jpg'), 'wb') as fp:
            fp.write(image_data)
        n += 1
    while n < 120:
        with open(os.path.join(img_dir, f'{n:06d}.jpg'), 'rb') as img:
            image_data = img.read()
        with open(os.path.join(f'{val_dir}/{n:06d}.jpg'), 'wb') as fp:
            fp.write(image_data)
        n += 1
