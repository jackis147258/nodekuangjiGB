let page = {
  page: 1,
  size: 50
}
let totalPage = 0
let profit = 0
let time = 11
let platform = []
let sport = []
let esport = []
let dataCode = 'profitarbitrage'
let accessToken = null
let requestURL = '/riskfree/profitarbitrage/list'
const platformItems = [
  {
    id: 1,
    title: '沙巴',
	titleEn: '12Bet',
    key: 72,
    checked: false
  }, {
    id: 2,
    title: '皇冠',
	titleEn: '188Bet',
    key: 66,
    checked: false
  }, {
    id: 3,
    title: '1xBet',
	titleEn: '1xBet',
    key: 74,
    checked: false
  }, {
    id: 4,
    title: 'Bet365',
	titleEn: 'Bet365',
    key: 26,
    checked: false
  }, {
    id: 5,
    title: '韦德[威廉]',
    titleEn: 'BetVictor',
    key: 55,
    checked: false
  }, {
    id: 6,
    title: '大发体育',
	titleEn: 'Nextbet',
    key: 88,
    checked: false
  }, {
    id: 7,
    title: 'GGBet',
	titleEn: 'GGBet',
    key: 175,
    checked: false
  }, {
    id: 8,
    title: '平博',
	titleEn: 'Pinnacle',
    key: 7,
    checked: false
  }, {
    id: 9,
    title: '利记',
	titleEn: 'SboBet',
    key: 25,
    checked: false
  }, {
    id: 10,
    title: '天宝博',
	titleEn: 'TempoBet',
    key: 184,
    checked: false
  }, {
    id: 11,
    title: 'NewBB体育',
	titleEn: 'VBet',
    key: 110,
    checked: false
  }, {
    id: 12,
    title: '易胜博',
	titleEn: 'YSB',
    key: 221,
    checked: false
  }
]

const categoryItems = [
  {
    category: 'sport',
    categoryName: '体育类',
    allChecked: true,
    items: [
      {
        id: 1,
        title: '足球',
        key: 15,
        checked: true
      }, {
        id: 2,
        title: '篮球',
        key: 4,
        checked: true
      }, {
        id: 3,
        title: '网球',
        key: 22,
        checked: true
      }, {
        id: 4,
        title: '棒球',
        key: 3,
        checked: true
      }, {
        id: 5,
        title: '美式足球',
        key: 0,
        checked: true
      }, {
        id: 5,
        title: '英式橄榄球',
        key: 20,
        checked: true
      }, {
        id: 6,
        title: '手球',
        key: 17,
        checked: true
      }, {
        id: 7,
        title: '乒乓球',
        key: 23,
        checked: true
      }, {
        id: 8,
        title: '羽毛球',
        key: 1,
        checked: true
      }, {
        id: 9,
        title: '排球',
        key: 24,
        checked: true
      }, {
        id: 10,
        title: '冰球',
        key: 18,
        checked: true
      }, {
        id: 11,
        title: '斯诺克',
        key: 21,
        checked: true
      }, {
        id: 12,
        title: '飞镖',
        key: 12,
        checked: true
      }
    ]
  }, {
    category: 'esport',
    categoryName: '电竞类',
    allChecked: true,
    items: [
      {
        id: 1,
        title: '反恐精英',
        key: 34,
        checked: true
      }, {
        id: 2,
        title: '刀塔2',
        key: 39,
        checked: true
      }, {
        id: 3,
        title: '王者荣耀',
        key: 45,
        checked: true
      }, {
        id: 4,
        title: '英雄联盟',
        key: 36,
        checked: true
      }
    ]
  }
]
const timeItems = [
  {
    id: 1,
    name: '12小时',
    key: 43200
  }, {
    id: 2,
    name: '16小时',
    key: 57600
  }, {
    id: 3,
    name: '1天',
    key: 86400
  }, {
    id: 4,
    name: '2天',
    key: 172800
  }, {
    id: 5,
    name: '7天',
    key: 604800
  }
]

const gridData = [
  {
    profit: {
      ratio: '10.0',
      timer: 'Live2分钟'
    },
    platform: [
      {
        platformName: '大发体育',
        categoryName: '足球'
      }, {
        platformName: 'Bet365',
        categoryName: '足球'
      }, {
        platformName: 'Bet365',
        categoryName: '足球'
      }
    ],
    timer: [
      {
        date: '01/07',
        time: '00:00'
      }, {
        date: '01/07',
        time: '00:00'
      }, {
        date: '01/07',
        time: '00:00'
      }
    ],
    project: [
      {
        game: 'FK Spartakas -FK Dembava',
        team: 'Football / Lithuania /II Lyga'
      }, {
        game: 'FKS Ukmerge -FK Dembava',
        team: 'Lithuania /II Lyga'
      }, {
        game: 'FKS Ukmerge -FK Dembava',
        team: 'Lithuania /II Lyga'
      }
    ],
    position: ['大于3', '小于3.5', '小于2.5'],
    price: [1.92, 2.00, 3.50],
    overvalueRate: ['+4.80%', '+4.79%', '+4.12%']
  }, {
    profit: {
      ratio: '7.34',
      timer: 'Live16分钟'
    },
    platform: [
      {
        platformName: 'NewBB体育',
        categoryName: '足球'
      }, {
        platformName: '天宝博',
        categoryName: '足球'
      }
    ],
    timer: [
      {
        date: '01/07',
        time: '01:00'
      }, {
        date: '01/07',
        time: '01:00'
      }
    ],
    project: [
      {
        game: 'SC 1903 Weimar -Carl Zeiss Jena',
        team: 'World - Club Friendlies'
      }, {
        game: 'SC 1903 Weimar -Carl Zeiss Jena',
        team: 'International Clubs - Club Friendlies'
      }
    ],
    position: ['主胜或平局 第2时间段', '2 第2时间段'],
    price: [13.00, 1.17],
    overvalueRate: ['+4.02%', '+4.09%']
  }, {
    profit: {
      ratio: '6.85',
      timer: 'Live2小时'
    },
    platform: [
      {
        platformName: '大发体育',
        categoryName: '排球'
      }, {
        platformName: '1xBet',
        categoryName: '排球'
      }
    ],
    timer: [
      {
        date: '01/07',
        time: '09:30'
      }, {
        date: '01/07',
        time: '09:30'
      }
    ],
    project: [
      {
        game: 'Serbia - Dominican Republic',
        team: 'Volleyball / International / Nations League, Women / Nations League, Women'
      }, {
        game: 'Serbia (Women) - Dominican Republic (Women)',
        team: 'FIVB Nations League, Women'
      }
    ],
    position: ['大于44.5 第1盘', '小于44.5 第1盘'],
    price: [2.06, 2.22],
    overvalueRate: ['+4.02%', '+4.09%']
  }, {
    profit: {
      ratio: '5.39',
      timer: 'Live4小时'
    },
    platform: [
      {
        platformName: '1xBet',
        categoryName: '篮球'
      }, {
        platformName: '利记',
        categoryName: '篮球'
      }
    ],
    timer: [
      {
        date: '01/07',
        time: '01:15'
      }, {
        date: '01/07',
        time: '01:15'
      }
    ],
    project: [
      {
        game: 'Iceland u20 (Women) - Sweden u20 (Women)',
        team: 'Northern Europe Championship U20. Women'
      }, {
        game: 'Sweden (w) U20 - lceland (w) U20',
        team: "Nordic Championship Women's U20 Basketball"
      }
    ],
    position: ['主队(+30.5) 含加时赛果', '主队(-30.5) 含加时果'],
    price: [2.67, 1.74]
  }, {
    profit: {
      ratio: '5.08',
      timer: 'Live3小时'
    },
    platform: [
      {
        platformName: '大发体育',
        categoryName: '足球'
      }, {
        platformName: '大发体育',
        categoryName: '足球'
      }, {
        platformName: 'NewBB体育',
        categoryName: '足球'
      }
    ],
    timer: [
      {
        date: '01/07',
        time: '02:30'
      }, {
        date: '01/07',
        time: '02:30'
      }, {
        date: '01/07',
        time: '02:30'
      }
    ],
    project: [
      {
        game: 'Melksham Town - Bristol Rovers',
        team: 'Football / International Clubs / Club Friendly Games'
      }, {
        game: 'Melksham Town - Bristol Rovers',
        team: "Football / International Clubs / Club Friendly Games"
      }, {
        game: 'Melksham Town FC - Bristol Rovers',
        team: "World . Club Friendlies"
      }
    ],
    position: ['进球:上半场得分更多', '进球:两个半场得分相等', '进球:下半场得分更多'],
    price: [3.35, 5.20, 2.17]
  }, {
    profit: {
      ratio: '3.37',
      timer: 'Live35分钟'
    },
    platform: [
      {
        platformName: 'Bet365',
        categoryName: '网球'
      }, {
        platformName: 'GGBet',
        categoryName: '网球'
      }
    ],
    timer: [
      {
        date: '30/06',
        time: '22:00'
      }, {
        date: '30/06',
        time: '22:00'
      }
    ],
    project: [
      {
        game: 'Martin Landaluce - Anton Matusevich',
        team: 'ITF M25 Bourg-en-Bresse'
      }, {
        game: 'Landaluce, Martin Matusevich, Anton',
        team: "ITF Frane F16. Men Sinales"
      }
    ],
    position: ['大于9.5 第1盘', '小于9.5 第1盘'],
    price: [2.20, 1.95]
  }
]

let calculationData = [{ left: 0.5, right: 0.5 }, { left: 0.5, right: "1.0" }, { left: "1.0", right: 1.5 }, { left: 0.5, right: 1.5 }]