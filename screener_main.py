import smart_value.tools.stock_screener as screener


def screener_data():
    """Return the company data from the screener

    :return: company data
    :rtype: DataFrame
    """

    # companies = ['6663.HK','1689.HK','1458.HK','1425.HK','1448.HK','2150.HK','6616.HK','1945.HK','1475.HK','1586.HK','0580.HK','1935.HK','9899.HK','9699.HK','6820.HK','8032.HK','0265.HK','1483.HK','1995.HK','9986.HK','2101.HK','2265.HK','1971.HK','6626.HK','6100.HK','1925.HK','1543.HK','9983.HK','6858.HK','1970.HK','0799.HK','6668.HK','0189.HK','0606.HK','0709.HK','0543.HK','3658.HK','1303.HK','1651.HK','8479.HK','2180.HK','1357.HK','2119.HK','6822.HK','0398.HK','0837.HK','0777.HK','2327.HK','6677.HK','6989.HK','1234.HK','0609.HK','9836.HK','0029.HK','0166.HK','6988.HK','1516.HK','1277.HK','1316.HK','1060.HK','3798.HK','1412.HK','1022.HK','9982.HK','0806.HK','1361.HK','2660.HK','1230.HK','6608.HK','1328.HK','2218.HK','6896.HK','0697.HK','0721.HK','1301.HK','6913.HK','3319.HK','0336.HK','1836.HK','1837.HK','2801.HK','0018.HK','0687.HK','0195.HK','0255.HK','0411.HK','0639.HK','3686.HK','0302.HK','1057.HK','1731.HK','0206.HK','0869.HK','1896.HK','0128.HK','2232.HK','2205.HK','1502.HK','1126.HK','6909.HK','6601.HK','0677.HK','9666.HK','0335.HK','9990.HK','2686.HK','1981.HK','3913.HK','0800.HK','0093.HK','8137.HK','0468.HK','1868.HK','0423.HK','1753.HK','0032.HK','2125.HK','3339.HK','1170.HK','1221.HK','0215.HK','6919.HK','2100.HK','1127.HK','0701.HK','3700.HK','0556.HK','0393.HK','3983.HK','0105.HK','2008.HK','0026.HK','0439.HK','0071.HK','1469.HK','0278.HK','2779.HK','0517.HK','0050.HK','0934.HK','0088.HK','0158.HK','0929.HK','0730.HK','0057.HK','0266.HK','0769.HK','0829.HK','1265.HK','0420.HK','0716.HK','3838.HK','1045.HK','0472.HK','2033.HK','1104.HK','1140.HK','1122.HK','0232.HK','0622.HK','0156.HK','0662.HK','0560.HK','0743.HK','0321.HK','0450.HK','1028.HK','1761.HK','0273.HK','3389.HK','0271.HK','6117.HK','0237.HK','0064.HK','0533.HK','0235.HK','0133.HK','8005.HK','0102.HK','1980.HK','3398.HK','0635.HK','0538.HK','0289.HK','2127.HK','1203.HK','3999.HK','0366.HK','0610.HK','0194.HK','0212.HK','0887.HK','3818.HK','1431.HK','0296.HK','0298.HK','1278.HK','1786.HK','0882.HK','2698.HK','1051.HK']
    # companies = ['2779.HK','0517.HK','0050.HK','0934.HK','0088.HK','0158.HK','0929.HK','0730.HK','0057.HK','0266.HK','0769.HK','0829.HK','1265.HK','0420.HK','0716.HK','3838.HK','1045.HK','0472.HK','2033.HK','1104.HK','1140.HK','1122.HK','0232.HK','0622.HK','0156.HK','0662.HK','0560.HK','0743.HK','0321.HK','0450.HK','1028.HK','1761.HK','0273.HK','3389.HK','0271.HK','6117.HK','0237.HK','0064.HK','0533.HK','0235.HK','0133.HK','8005.HK','0102.HK','1980.HK','3398.HK','0635.HK','0538.HK','0289.HK','2127.HK','1203.HK','3999.HK','0366.HK','0610.HK','0194.HK','0212.HK','0887.HK','3818.HK','1431.HK','0296.HK','0298.HK','1278.HK','1786.HK','0882.HK','2698.HK','1051.HK']
    companies = ['0677.HK', '6822.HK']

    screener.collect_data(companies, "yf")

if __name__ == '__main__':

    screener_data()
    # screener.merge_data()