# Welcome  

## Using

 - Get Xor Keys from libil2cpp.so (you can xorkeys offset from IDA and find keys in HxD)
 - Paste it in .py file
 
 ``` Note: in new Standoff 2 versions you no need to decrypt metadata ```

![XorKeysExample](https://user-images.githubusercontent.com/33353036/202772948-65f5c5a9-9d1e-407f-a552-4960f4ff73ce.png)
 - Run .py file, input metadata path and save path
 - Profit

## How to get Xor Keys without IDA

 - Open global-metadata.dat in HxD
 - Search (CTRL + F) hex-value "C8 C1 BB D4 BF F5 47 46 94 95 2E 5C 0F 20 F7 5D FF FF FF FF 03"

![HxD](https://user-images.githubusercontent.com/33353036/202774308-220c71ca-a38c-4c19-9c39-12c7dcb015b0.png)
 - Now select 2048 (800 in hex) values after value 46 (F in decoded text)
 
 ![asdasdasd](https://user-images.githubusercontent.com/33353036/202774679-64ea834b-88d6-4a6b-984d-1199ec3e8552.png)
 
![zxczxc12](https://user-images.githubusercontent.com/33353036/202775047-78f67874-d591-44a0-8b0e-98e9b70098c0.png)
 - Now сopy all values and create new file in HxD and paste it
 
 ![dfhw2](https://user-images.githubusercontent.com/33353036/202775343-4e39098c-efd0-4a6f-99c4-c4375c61eb81.png)
 - And export this as C file
 
 ![hq7hd781](https://user-images.githubusercontent.com/33353036/202775587-16846bf0-bea9-4486-aa83-ddaab3ac533f.png)
 - Its all, now you can paste xorkeys in .py file
 
 ![изображение](https://user-images.githubusercontent.com/33353036/202775899-d8236c9a-90a4-4d7e-b615-7d99c1e21b4f.png)
