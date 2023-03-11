# Bus Interrogation Tunnel

[BIT 班车](http://hqapp1.bit.edu.cn/newbanche/)查询接口。

```shell
$ pdm install
$ pdm run python -m bus_interrogation_tunnel
{'code': '1',
 'message': 'ok',
 'data': {'reserved_count': 48,
          'reservation_num': 3,
          'reserved_seat_number': ['3', '10', '14', '5', '26', '22', '15', '35',
                                   '4', '37', '51', '27', '32', '19', '8', '36',
                                   '34', '39', '30', '42', '33', '20', '11',
                                   '7', '23', '38', '50', '47', '40', '45',
                                   '16', '41', '24', '43', '48', '12', '21',
                                   '28', '6', '44', '17', '18', '13', '9', '31',
                                   '25', '29', '46'],
          'is_full': 1}}
```
