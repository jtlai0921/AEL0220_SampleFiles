for i in range(1,10):     # 九九乘表 比較實際的寫法
    for j in range(1,10): # 通常縮排的空格數為 4 個，
                          # 其實用 2 到 6 個空格之間都可
        print("%3d" % (i*j), end='') # %3d每個數值以十進位佔三格
    print('')             # 換行 或用 '\n' 也可
