sentece='[[1, "Hung", "192.168.47.1", "https://genk.mediacdn.vn/k:thumb_w/640/2016/photo-1-1473821552147/top6suthatcucsocvepikachu.jpg"], [2, "Kiet", "192.168.47.1", "https://genk.mediacdn.vn/k:thumb_w/640/2016/photo-1-1473821552147/top6suthatcucsocvepikachu.jpg"], [3, "Bu", "192.168.47.1", "https://genk.mediacdn.vn/k:thumb_w/640/2016/photo-1-1473821552147/top6suthatcucsocvepikachu.jpg"], [4, "Nghia", "192.168.47.1", "https://genk.mediacdn.vn/k:thumb_w/640/2016/photo-1-1473821552147/top6suthatcucsocvepikachu.jpg"], [9, "sadas", "192.168.111.137", ""], [10, "iaohdioaw", "192.168.111.137", ""], [11, "LMNLM", "192.168.111.137", ""], [12, "asdasd", "192.168.111.137", ""]]'
arr=sentece.split("], [")
arr[0]=arr[0][2:]
arr[-1]=arr[-1][:-2]
for i in range(len(arr)):
    arr[i]=arr[i].split(', ')
    for ii in range(4):
        arr[i][ii]=arr[i][ii].strip("\"")
    arr[i][0]=int(arr[i][0])
print(arr)
    