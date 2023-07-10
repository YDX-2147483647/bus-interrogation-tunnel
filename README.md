# 🚌 Bus Interrogation Tunnel (`bitbus`)

[![best of BITs](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/YDX-2147483647/best-of-bits/main/config/badge/v1.json)](https://github.com/YDX-2147483647/best-of-bits)

[BIT 班车](http://hqapp1.bit.edu.cn/newbanche/)查询接口。

> **Note**
>
> 只有查询功能，故无需登录。

## 🧪 例子

（要先克隆仓库，[`pdm install`](https://pdm.fming.dev/latest/usage/cli_reference/#exec-0--install)）

### 🚍 查询车次

```
$ pdm run bitbus /vehicle/get-list date==2023-03-13
{
    'count': 52,
    'code': '0',
    'message': 'ok',
    'data': [
        {
            'pkid': 3338,
            'id': '2217130562077421589',
            'shuttle_type': 3,
            'car_number': '京ADG889',
            'name': '良乡校区-中关村校区',
            'train_number': '',
            'service_time': '1,2,3,4,5',
            'origin_address': '良乡校区',
            'end_address': '中关村校区',
            'intermediate_site': None,
            'origin_time': '06:20',
            'end_time': '07:10',
            'reservation_num_able': 51,
            'type': 0,
            'teacher_ticket_price': '10.0',
            'student_ticket_price': '6.0'
        },
…
}
```

也可以筛选始末站：

```shell
$ pdm run bitbus /vehicle/get-list date==2023-03-13 address==良乡校区->中关村校区
```

### 💺 查询座位

```
$ pdm run bitbus /vehicle/get-reserved-seats id==2208639427336042078 date==2023-03-11
{'code': '1',
 'message': 'ok',
 'data': {'reserved_count': 48,
          'reservation_num': 3,
          'reserved_seat_number': ['3', '10', '14', …],
          'is_full': 1}}
```

## 🛠️ 开发

```shell
$ pdm install
```

```
$ pipx install pre-commit  # Alternate: python -m pip install pre-commit
$ pre-commit install
$ pdm run lint
```
