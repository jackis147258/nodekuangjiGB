const domain = "http://www.youdao.love" //'http://47.100.22.123:8101'  
let token = null 
$(document).ready(function () {
  loadPlatform()
  loadSelectOption()
  loadCategory()
  loadCalculation()
  platformSelectInit()
  getData("current")
  setTimeout(function () {
    $('.container-left-head-platform-all-cover').bind('click', platformSelectAll)
	//$('.container-left-head-platform-all-text').bind('click', platformSelectAll2)
    $('.container-left-head-platform-content-item').bind('click', changePlatformItem)
    $('.container-left-head-data-content-item').bind('click', changeDataItem)
    $('.container-left-head-refresh-content').bind('click', refresh)
    $('.container-left-head-profit-up-body-title-select').bind('change', changeTime)
    $('.container-left-head-profit-down-body-title-input').bind('blur', changeProfit)
    $('.container-left-head-lang-content-body-up').bind('click', changeLanguage)
    $('.container-left-head-lang-content-body-down').bind('click', changeLanguage)
    //$('.container-right-category-item-content-all').bind('click', categorySelectAll)
    $('.container-right-category-item-content-body-item').bind('click', changeSportItem)
    //$('body').on('click', '.container-left-body-content-item-project-item-up', copyData)
    //$('body').on('click', '.container-left-body-content-item-project-item-down', copyData)
    //$('.container-left-footer-page-previous').bind('click', previousPage)
    //$('.container-left-footer-page-next').bind('click', nextPage)
    $('.container-left-head-selective-content-up-refresh').bind('click', refresh)
    $('.material-checkbox').bind('change', AutoRefresh)
    $(".container-left-head-selective-content-up-interval-inputs>input").bind('input', AutoRefreshTimes)
  }, 500)
  

})



function copyData(text,type) {

	navigator.clipboard.writeText(text).then(function() {
		//console.log("Text copied to clipboard successfully!");
		let str = ""
		if(type == 1){
			str = "<div class='copy-show'>已复制至剪切板（赛事）</div>"
		}else if(type == 2){
			str = "<div class='copy-show'>已复制至剪切板（主队名）</div>"
		}else{
			str = "<div class='copy-show'>已复制至剪切板</div>"
		}
		$(".copy").html(str)
		
		let timer = setTimeout(function () {
			$(".copy").html("")
		
		}, 2000)
	}, function(err) {
		//console.error("Failed to copy text: ", err);
	});
	
	/*
	$(this).text().select()
	document.execCommand('copy')
	*/
}

var scrollTop;
function noScroll() {                                                                                    
    scrollTop = document.body.scrollTop || document.documentElement.scrollTop;                         
    document.body.style.cssText += 'position:fixed;width:100%;top:-'+scrollTop+'px;';                    
}

function returnScroll() {                                                                                
    document.body.style.position = '';                                                                    
    document.body.style.top = '';                                                                         
    document.documentElement.scrollTop = scrollTop;                                                      
}

function showLoading() {
  $('.container-loading').css("display","block")
  $('.container-loading').show()
  if($('.container-loading').css("display") == "none" || $('.container-loading').css("display") == ""){
	  $('.container-loading').toggle()
  }
  noScroll()
}

function hideLoading() {
  $('.container-loading').hide()
   if($('.container-loading').css("display") == "block"){
	  $('.container-loading').toggle()
  }
  returnScroll()
}

function previousPage() {
  if (page.page > 1) {
    page.page = page.page - 1
  }
  getData("current")
}

function nextPage() {
  if (page.page < totalPage) {
    page.page = page.page + 1
  }
  getData("current")
}

function platformSelectInit() {
	//console.log("platformSelectInit")
	/*
  if ('crownzone' === dataCode) {
    return
  }*/
  const key = 72
  let className = '.container-left-head-platform-all-input'
  let els = $(className)
  let elementItems = $('.container-left-head-platform-content-item').siblings()
  for(let i = 0; i < 1; i++) {
	  $(elementItems[i]).children('input[type="checkbox"]').attr('checked', true)
	  $(elementItems[i]).children('input[type="checkbox"]').prop('checked', true)
	  $(elementItems[i]).addClass("container-left-head-platform-content-item-active")
	  $($(elementItems[i]).children()[2]).addClass("container-left-head-platform-content-item-label2-active")
  }
  platform.push(key)

}

function platformSelectAll() {
	platform = []
	//console.log("platformSelectAll")
	/*
  if ('crownzone' === dataCode) {
    return
  }
  */
  let className = '.container-left-head-platform-all-input'
  const checked = $(className).prop('checked') 
  // console.log("checked:",checked)
  let flag = !checked
 
  $(className).attr('checked', flag)   
  $(className).prop('checked', flag)   
  //let elementItems = $('.container-left-head-platform-content-item').siblings()
  let elementItems = $('.container-left-head-platform-content-item')
  for (let i = 0; i < elementItems.length; i++) {
    $(elementItems[i]).children('input[type="checkbox"]').attr('checked', flag)
	$(elementItems[i]).children('input[type="checkbox"]').prop('checked', flag)
	if(flag){
		$(elementItems[i]).addClass("container-left-head-platform-content-item-active")
		$($(elementItems[i]).children()[2]).addClass("container-left-head-platform-content-item-label2-active")

	}else{	
	
		$(elementItems[i]).removeClass("container-left-head-platform-content-item-active")
		$($(elementItems[i]).children()[2]).removeClass("container-left-head-platform-content-item-label2-active")
	}
  }
  if (flag) {
    platformItems.forEach(item => platform.push(item.key))
  } else {
    platform = []
  }
  
  //console.log(platform)
}


function changePlatformItem() {
  //console.log("changePlatformItem")
  /*
  if ('crownzone' === dataCode) {
    return
  }*/
  const key = Number($(this).attr('key'))
  const checked = $(this).children('input[type="checkbox"]').prop('checked')
  console.log("checked:",checked)
  const flag = checked
  $(this).children('input[type="checkbox"]').attr('checked', flag)
  $(this).children('input[type="checkbox"]').prop('checked', flag)
  const index = platform.findIndex(item => item === key)
  if (flag) {
    if (index === -1) {
      platform.push(key)
    }
	 $(this).addClass("container-left-head-platform-content-item-active")
	 $($(this).children()[2]).addClass("container-left-head-platform-content-item-label2-active")
  } else {
    if (index !== -1) {
      platform.splice(index, 1)
    }
	$(this).removeClass("container-left-head-platform-content-item-active")
	$($(this).children()[2]).removeClass("container-left-head-platform-content-item-label2-active")
  }
}

function categorySelectAll(categoryType) {
	//console.log("categorySelectAll")
	//console.log("categoryType：",categoryType)
	if(categoryType == 'sport'){
		const checked = $('.container-right-category-item-content-all-input-sport').prop('checked') 
		//console.log("checked：",checked)
		let flag = !checked
		$('.container-right-category-item-content-all-input-sport').attr('checked', flag) 
		let elementItems = $('.container-right-category-item-content-body-item-sport')		 
		for (let i = 0; i < elementItems.length; i++) {
			$(elementItems[i]).children('input[type="checkbox"]').attr('checked', flag)
			$(elementItems[i]).children('input[type="checkbox"]').prop('checked', flag)
			if(flag){
				$(elementItems[i]).addClass("container-right-category-item-content-body-item-active")
				$($(elementItems[i]).children()[2]).addClass("container-right-category-item-content-body-item-label2-active")
		
			}else{	
			
				$(elementItems[i]).removeClass("container-right-category-item-content-body-item-active")
				$($(elementItems[i]).children()[2]).removeClass("container-right-category-item-content-body-item-label2-active")
			}
		}
		if (flag) {
			sport = []
			const items = categoryItems.find(item => item.category === categoryType).items
			items.forEach(item => {
				sport.push(item.key)
			})
		} else {
			sport = []
		}
  
  
	}else if(categoryType == 'esport'){
		const checked = $('.container-right-category-item-content-all-input-esport').prop('checked') 
		let flag = !checked
		$('.container-right-category-item-content-all-input-esport').attr('checked', flag)  
		let elementItems = $('.container-right-category-item-content-body-item-esport')
		for (let i = 0; i < elementItems.length; i++) {
			$(elementItems[i]).children('input[type="checkbox"]').attr('checked', flag)
			$(elementItems[i]).children('input[type="checkbox"]').prop('checked', flag)
			if(flag){
				$(elementItems[i]).addClass("container-right-category-item-content-body-item-active")
				$($(elementItems[i]).children()[2]).addClass("container-right-category-item-content-body-item-label2-active")
		
			}else{	
				$(elementItems[i]).removeClass("container-right-category-item-content-body-item-active")
				$($(elementItems[i]).children()[2]).removeClass("container-right-category-item-content-body-item-label2-active")
			}
		}
		if (flag) {
			esport = []
			const items = categoryItems.find(item => item.category === categoryType).items
			items.forEach(item => {
				esport.push(item.key)
			})
		} else {
			esport = []
		}
	}

  
  //console.log(sport)
  //console.log(esport)
}


// 数据项切换
function changeDataItem() {
	//console.log("changeDataItem")
  $('.container-left-head-data-content-item-selected').removeClass('container-left-head-data-content-item-selected')
  $(this).toggleClass('container-left-head-data-content-item-selected')
  const code = $(this).attr('code')
  dataCode = code


  // 选中价值篮球处理逻辑
  if ('valueBasketball' === code) {
    $(".container-left-head-platform-form,.container-left-head-profit,.container-left-head-lang,.container-left-head-refresh,.container-right").hide()
    $(".container-left").css("width", "100%")
    $(".container-left-head-platform-image,.container-left-head-selective").show()
    if ($(".material-checkbox>input")[0].checked) {

    }
  } else {
    $(".container-left-head-platform-form,.container-left-head-profit,.container-left-head-lang,.container-left-head-refresh,.container-right").show()
    $(".container-left-head-platform-image,.container-left-head-selective").hide()
  }



  if ('profitarbitrage' === code) {
    requestURL = '/riskfree/profitarbitrage/list'
  } else if ('intervalprofit' === code) {
    requestURL = '/riskfree/intervalprofit/list'
  } else if ('crownzone' === code) {
    requestURL = '/riskfree/crownzone/list'
    $('.container-left-head-platform-all-input').attr('checked', false)
	$('.container-left-head-platform-all-input').prop('checked', false)
    const childrenElements = $('.container-left-head-platform-content').children()
    for (let i = 0; i < childrenElements.length; i++) {
      const key = Number($(childrenElements[i]).attr('key'))
      if (66 === key) {
        $(childrenElements[i]).children('input[type="checkbox"]').attr('checked', true)
		$(childrenElements[i]).children('input[type="checkbox"]').prop('checked', true)
		$(childrenElements[i]).addClass("container-left-head-platform-content-item-active")
		$($(childrenElements[i]).children()[2]).addClass("container-left-head-platform-content-item-label2-active")
        platform = [key]
      }else{
		$(childrenElements[i]).children('input[type="checkbox"]').attr('checked', false)
		$(childrenElements[i]).children('input[type="checkbox"]').prop('checked', false)
		$(childrenElements[i]).removeClass("container-left-head-platform-content-item-active")
		$($(childrenElements[i]).children()[2]).removeClass("container-left-head-platform-content-item-label2-active")
	  }
    }
  } else if ('valuebeyonddata' === code) {
    requestURL = '/riskfree/valuebeyonddata/list'
  } else if ('valueBasketball' === code) {

    requestURL = '/valueBasketball/select'
  }
  loadTableColumn()
}

function changeTime() {
  time = $(this).val()
}

function changeProfit() {
  profit = Number($(this).val())
}

var language = "EN"
// 切换语言
function changeLanguage() {
  $('.container-left-head-lang-content-body-selected').removeClass('container-left-head-lang-content-body-selected')
  $(this).toggleClass('container-left-head-lang-content-body-selected')
  const lang = $(this).attr('lang')
  language = lang
  getDataRender()
  //loadPlatform()
  //$('.container-left-head-platform-content-item').bind('click', changePlatformItem)
  //platformSelectInit()
  //$('.container-left-head-platform-all-input').attr('checked', false)
  //getData("current")
  
}


function changeSportItem() {
 //console.log("changeSportItem")
  let key = Number($(this).attr('key'))
  
  const category = $(this).attr('category')
  const checked = $(this).children('input[type="checkbox"]').prop('checked')
  const flag = !checked
  $(this).children('input[type="checkbox"]').attr('checked', flag)
  $(this).children('input[type="checkbox"]').prop('checked', flag)
  if ('sport' === category) {
    const index = sport.findIndex(item => item === key)
    if (flag) {
      if (index === -1) {
        sport.push(key)
      }
	  	$(this).addClass("container-right-category-item-content-body-item-active")
		$($(this).children()[2]).addClass("container-right-category-item-content-body-item-label2-active")
    } else {
      if (index !== -1) {
		  
        sport.splice(index, 1)
      }
	  $(this).removeClass("container-right-category-item-content-body-item-active")
	  $($(this).children()[2]).removeClass("container-right-category-item-content-body-item-label2-active")
    }
  } else if ('esport' === category) {
    const index = esport.findIndex(item => item === key)
    if (flag) {
      if (index === -1) {
        esport.push(key)
      }
	  $(this).addClass("container-right-category-item-content-body-item-active")
	  $($(this).children()[2]).addClass("container-right-category-item-content-body-item-label2-active")
    } else {
      if (index !== -1) {
        esport.splice(index, 1)
      }
	  $(this).removeClass("container-right-category-item-content-body-item-active")
	  $($(this).children()[2]).removeClass("container-right-category-item-content-body-item-label2-active")
    }
  }
  //console.log(sport)
   //console.log(esport)
}


function getToken(callback) {
  if (!accessToken) {
    login(token => {
      callback && callback(token)
    })
    return
  }
  callback && callback(accessToken)
}

function login(callback) {
  $.ajax({
    url: `${domain}/login`,
    type: 'POST',
    dataType: 'JSON',
    contentType: 'application/json; charset=utf8',
    data: JSON.stringify({
      username: 'admin',
      password: 'admin123',
      code: 3
    }),
    success: function (res) {
      const { token, code, msg } = res || {}
      if (code !== 200) {
        alert(msg)
        return
      }
      accessToken = token
      callback && callback(token)
    }
  })
}


var pagePreRequestUrl = ""
var pageNextRequestUrl = ""
var profitDataArr = []// 利润对象列表：数据要根据利润分组
function getData(pageType) {
	if(platform=="" || platform==undefined || platform.length < 0){
		alert("请选择平台")
		return
	}
	showLoading()

	let paramItems = [`pageSize=${page.size}`, `pageNum=${page.page}`]
    paramItems.push(`profit=${profit}`)
    time && paramItems.push(`time=${time}`)
    if (platform && platform.length > 0) {
      paramItems.push(`platform=${platform.join(',')}`)
    }
    let moveType = []
    if (sport && sport.length > 0) {
      moveType.push(`${sport.join(',')}`)
    }
    if (esport && esport.length > 0) {
      moveType.push(`${esport.join(',')}`)
    }
    if (moveType && moveType.length > 0) {
      paramItems.push(`moveType=${moveType.join(',')}`)
    }
	
	let reqURL = domain + "/app1/htmlInfo/"
	let reqData = {"pageSize":`${page.size}`,"pageNum":`${page.page}`,'profit':`${profit}`,'time':`${time}`,'platform':`${platform}`,'moveType':`${moveType}`}
	let reqType = "POST"
	if(pageType == "current" || pageType == null || pageType == undefined || pageType == ""){
		reqURL = domain + "/app1/htmlInfo/"
	}else if(pageType == "pre"){
		reqURL = domain + "/app1/nextPage/?page="+pagePreRequestUrl
		reqData = ""
		reqType = "POST"
	}else if(pageType == "next"){
		reqURL = domain + "/app1/nextPage/?page="+pageNextRequestUrl
		reqData = ""
		reqType = "POST"
	}
	$.ajax({
      url: `${reqURL}`,   
      headers: {
		'User-Agent':'Apifox/1.0.0 (https://apifox.com)',
		'Host':'www.youdao.love',
		'Connection':'keep-alive',
        'Content-Type': 'application/json', 
        'Accept': '*/*', 
		'Accept-Encoding':'gzip, deflate, br'

      },
      type: reqType,
	  dataType: 'JSON',
	  data: reqData,
      contentType: 'application/json; charset=utf8',
	  ajaxGridOptions: {
           xhrFields: { 
                  withCredentials: true
            }
      }, 
      crossDomain: true,
      complete: function(){
		  hideLoading()
	  },  
      success: function (res) {
		$('.container-left-body-content').html("") 
		profitDataArr = []
		  
		// res的data是一个数组，分为三部分，第一部分是数据，第二、三部分是分页
		profitDataArr = JSON.parse(res.data)[0]
		console.log(profitDataArr)
		pagePreRequestUrl = JSON.parse(res.data)[2]
		pageNextRequestUrl = JSON.parse(res.data)[1]

		setTimeout(()=>{
			getDataRender()
		},1)
		
		
        const { data = [], total = 0 } = res || {}
        if (total / page.size > parseInt(total / page.size)) {
          totalPage = parseInt(total / page.size) + 1
        } else {
          totalPage = parseInt(total / page.size)
        }
		

		//$('.container-left-footer-page-previous').attr('href',"javascript:void(0);")
		//$('.container-left-footer-page-next').attr('href',"javascript:void(0);")
		//console.log(data)
		//$('.container-left-body-content').html(data)
		/**
        const dataItem = data.reduce((group, item) => {
          const { groupType } = item
          group[groupType] = group[groupType] ?? []
          group[groupType].push(item)
          return group
        }, {})
        let gridDataItems = []
        Object.keys(dataItem).forEach(key => {
          const items = dataItem[key] || []
          let profit = {}, platform = [], timer = [], project = [], position = [], odds = [], overvalueRate = []
          items.forEach(item => {
            Object.assign(profit, { ratio: item.profit ? item.profit.replace('%', '') : 0, timer: item.liveTime || profit.timer || '-' })
            platform.push({ platformName: item.platformName || item.platform || '-', categoryName: item.moveTypeName || item.moveType || '-' })
            timer.push({ date: item.kickOffTime ? item.kickOffTime.substr(0, 5) : '', time: item.kickOffTime ? item.kickOffTime.substr(5) : '' })
            project.push({ game: item.projectDescriptionCh, team: item.projectCh })
            position.push(`${item.arbitrageTrading} ${item.arbitrageTradingDetails || ''}`)
            odds.push(item.odds)
            overvalueRate.push(item.overvalueRate || '-')
          })
          gridDataItems.push({ profit, platform, timer, project, position, odds, overvalueRate })
        })
        loadGrid(gridDataItems)
		*/
      }
    })
/**
  getToken(token => {
    let paramItems = [`pageSize=${page.size}`, `pageNum=${page.page}`]
    paramItems.push(`profit=${profit}`)
    time && paramItems.push(`time=${time}`)
    if (platform && platform.length > 0) {
      paramItems.push(`platform=${platform.join(',')}`)
    }
    let moveType = []
    if (sport && sport.length > 0) {
      moveType.push(`${sport.join(',')}`)
    }
    if (esport && esport.length > 0) {
      moveType.push(`${esport.join(',')}`)
    }
    if (moveType && moveType.length > 0) {
      paramItems.push(`moveType=${moveType.join(',')}`)
    }
    showLoading()
    $.ajax({
      url: `${domain}${requestURL}?${paramItems.join('&')}`,
      headers: {
        Authorization: token
      },
      type: 'GET',
      dataType: 'JSON',
      contentType: 'application/json; charset=utf8',
      complete: hideLoading,
      success: function (res) {
        const { data = [], total = 0 } = res || {}
        if (total / page.size > parseInt(total / page.size)) {
          totalPage = parseInt(total / page.size) + 1
        } else {
          totalPage = parseInt(total / page.size)
        }
        const dataItem = data.reduce((group, item) => {
          const { groupType } = item
          group[groupType] = group[groupType] ?? []
          group[groupType].push(item)
          return group
        }, {})
        let gridDataItems = []
        Object.keys(dataItem).forEach(key => {
          const items = dataItem[key] || []
          let profit = {}, platform = [], timer = [], project = [], position = [], odds = [], overvalueRate = []
          items.forEach(item => {
            Object.assign(profit, { ratio: item.profit ? item.profit.replace('%', '') : 0, timer: item.liveTime || profit.timer || '-' })
            platform.push({ platformName: item.platformName || item.platform || '-', categoryName: item.moveTypeName || item.moveType || '-' })
            timer.push({ date: item.kickOffTime ? item.kickOffTime.substr(0, 5) : '', time: item.kickOffTime ? item.kickOffTime.substr(5) : '' })
            project.push({ game: item.projectDescriptionCh, team: item.projectCh })
            position.push(`${item.arbitrageTrading} ${item.arbitrageTradingDetails || ''}`)
            odds.push(item.odds)
            overvalueRate.push(item.overvalueRate || '-')
          })
          gridDataItems.push({ profit, platform, timer, project, position, odds, overvalueRate })
        })
        loadGrid(gridDataItems)
      }
    })
  })
  */
 
}

function getDataRender(){
	var renderHtmlContent = "<div class='body-content'>"
		if(profitDataArr && profitDataArr.length>0){
			for(let i=0;i<profitDataArr.length;i++){// 遍历主要数据数组
					let successCount = 0
					let tempHtmlContent1 = ""
					
					// 构建第一列渲染数据  利润、时间、计算器icon
					tempHtmlContent1 += "<div class='body-content-row-block'>"
					
					tempHtmlContent1 += "<div class='body-content-row-wrap-left'>"
					tempHtmlContent1 += "<div class='body-content-row-wrap-left-el'>"
					tempHtmlContent1 += "<div class='body-content-row-wrap-left-el-1'>"+profitDataArr[i].profitText+"</div>"
					tempHtmlContent1 += "<div class='body-content-row-wrap-left-el-2'>Live"+profitDataArr[i].ageText+"</div>"
					tempHtmlContent1 += "<div class='body-content-row-wrap-left-el-3'><div class='body-content-row-wrap-left-el-3-show'></div></div>"
					tempHtmlContent1 += "</div>"
					tempHtmlContent1 += "</div>"
					
					tempHtmlContent1 += "<div class='body-content-row-wrap-right'>"
					
					let theProfitDatas = profitDataArr[i].td
					for(let j=0;j<theProfitDatas.length;j++){// 遍历每组利润的数据对象
						let dataObj = theProfitDatas[j]
						
						if(dataObj['eventA'] =="" || dataObj['eventSpan'] ==""){
							continue
						}
						
						//let renderFlag2 = true
						let tempHtmlContent2 = "<div class='body-content-row-wrap'>"

						successCount++
						//let keys = Object.keys(dataObj)
						//let values = Object.values(dataObj)
						//console.log(dataObj)
						//console.log(values)
						
							
						let el2 = "<div class='el-2'>"
						let theValue21 = strLanguageConvert(dataObj.booker,language)
						theValue21 = strLanguageFilterate(theValue21,language)
						el2 += "<div class='el-inner el-2-1'>"+theValue21+"</div>"
						let theValue22 = strLanguageConvert(dataObj.bookerspanText,language)
						theValue22 = strLanguageFilterate(theValue22,language)
						el2 += "<div class='el-inner el-2-2'>"+theValue22+"</div>"
						el2 += "</div>"
						
						
						let el3 = "<div class='el-3'>"
						let theValue31 = strLanguageConvert(dataObj.time.substring(0,5),language)
						theValue31 = strLanguageFilterate(theValue31,language)
						el3 += "<div class='el-inner el-3-1'>"+theValue31+"</div>"
						let theValue32 = strLanguageConvert(dataObj.time.substring(5,dataObj.time.length),language)
						theValue32 = strLanguageFilterate(theValue32,language)
						el3 += "<div class='el-inner el-3-2'>"+theValue32+"</div>"
						el3+= "</div>"
						
					
						let el4 = "<div class='el-4'>"
						let theValue41 = strLanguageConvert(dataObj['eventA'],language)
						theValue41 = strLanguageFilterate(theValue41,language)
						el4 += "<div class='el-inner el-4-1'>"+theValue41+"</div>"
						let theValue42 = strLanguageConvert(dataObj['eventSpan'],language)
						theValue42 = strLanguageFilterate(theValue42,language)
						el4 += "<div class='el-inner el-4-2'>"+theValue42+"</div>"
						el4+= "</div>"
						
						/*
						let el4 = "<div class='el-4'>"
						let value4Arr = null
						if(dataObj['eventA'] && dataObj['eventA'].includes(" - ")){
							value4Arr = dataObj['event'].split(" - ")
							console.log("value4Arr：",value4Arr)
						}else if(dataObj['event'] && dataObj['event'].includes(" ")){
							value4Arr = dataObj['event'].split(" ")
						}
						if(value4Arr && value4Arr.length>0){
							for(let k=0;k<value4Arr.length;k++){
								let index = k+1
								let theValue = strLanguageConvert(value4Arr[k],language)
								theValue = strLanguageFilterate(theValue,language)
								let el4_x = ""
								
								if(theValue && theValue.toString().trim()!=""){
									el4_x = "<div class='el-inner el-4-"+index+"'>"+theValue+"</div>"
								}
								
								el4 += el4_x
							}
						}
						el4 += "</div>"
						*/
						
						let theValue5 = strLanguageConvert(dataObj.coeff,language)
						theValue5 = strLanguageFilterate(theValue5,language)
						if(theValue5.includes("ordinal")){
							theValue5 = theValue5.substring(0,1)
						}
						let el5 = "<div class='el-5'><div class='el-5-img'></div><div>"+theValue5+"</div></div>"
						
						let theValue6 = strLanguageConvert(dataObj.value,language)
						theValue6 = strLanguageFilterate(theValue6,language)
						let el6 = "<div class='el-6'>"+theValue6+"</div>"

						let renderRow = "<div class='body-content-row'>"+el2+el3+el4+el5+el6+"</div>"
						tempHtmlContent2 += renderRow
						tempHtmlContent2 += "</div>"
						
						
						tempHtmlContent1 += tempHtmlContent2
						/*
						if(renderFlag2){
							
						}
						*/
						
					}// 遍历end
					
					tempHtmlContent1 += "</div>"
					tempHtmlContent1 += "</div>"
					if(successCount > 0){
						renderHtmlContent += tempHtmlContent1
					}
					
					
					
					
					
				
			}// 遍历end
		}
		
		renderHtmlContent += "</div>"
		$('.container-left-body-content').html(renderHtmlContent)
		
		 $(".body-content-row-block").off().click(function(){
			$(".body-content-row-block").removeClass("body-content-row-block-active")
			$(this).addClass("body-content-row-block-active")
		})
		$(".container-left-footer-page-previous").off().click(function(){getDataPre()})
		$(".container-left-footer-page-next").off().click(function(){getDataNext()})
		$('.el-4-1').off().click(function(){copyData($(this).text(),1)})
		$('.el-4-2').off().click(function(){copyData($(this).text(),2)})
}

function getDataPre(){
	getData("pre")
}
function getDataNext(){
	getData("next")
}
function loadPlatform() {
  let platform = ''
  platformItems.forEach((item, index) => {
    platform += '<div class="container-left-head-platform-content-item" key="' + item.key + '">'
    //platform += '<input type="checkbox" disabled id="checkbox_' + (index + 1) + '" class="container-left-head-platform-content-item-checkbox container-checkbox" />'
	platform += '<input type="checkbox" id="checkbox_' + (index + 1) + '" class="container-left-head-platform-content-item-checkbox container-checkbox" />'
    platform += '<label for="checkbox_' + (index + 1) + '" class="checkbox container-left-head-platform-content-item-label1"></label>'
	platform += '<label class="container-left-head-platform-content-item-label2">' + item.title + '</label>'
    platform += '</div>'
  })
  $('.container-left-head-platform-content').html(platform)
}

function loadSelectOption() {
  let option = ''
  timeItems.forEach(item => {
    option += '<option value="' + item.key + '">' + item.name + '</option>'
  })
  $('.container-left-head-profit-up-body-title-select').html(option)
}

function loadCalculation() {
  let calculation = ''
  for(let i=0; i< calculationData.length; i++){
	let index = i+1
	calculation += '<div class="container-right-calc-content-item container-right-calc-content-item-'+index+'" >'
    calculation += '<div class="container-right-calc-content-item-left">'
    calculation += '<div class="container-right-calc-content-item-left-up"></div>'
    calculation += '<div class="container-right-calc-content-item-left-number">' + calculationData[i].left + '</div>'
    calculation += '<div class="container-right-calc-content-item-left-up"></div>'
    calculation += '</div>'
    calculation += '<div class="container-right-calc-content-item-center">---</div>'
    calculation += '<div class="container-right-calc-content-item-right">'
    calculation += '<div class="container-right-calc-content-item-right-up"></div>'
    calculation += '<div class="container-right-calc-content-item-right-number">' + calculationData[i].right + '</div>'
    calculation += '<div class="container-right-calc-content-item-right-up"></div>'
    calculation += '</div>'
    calculation += '</div>'
  }
	
  $('.container-right-calc-content').html(calculation)
  
  
  $('.container-right-calc-content-item-1').off().click(function(){
	  window.open("./calculator/ydty0.html")
  })
  $('.container-right-calc-content-item-2').off().click(function(){
	  window.open("./calculator/ydty1.html")
  })
  $('.container-right-calc-content-item-3').off().click(function(){
	  window.open("./calculator/ydty2.html")
  })
  $('.container-right-calc-content-item-4').off().click(function(){
	  window.open("./calculator/ydty3.html")
  })
}

function loadCategory() {
  let category = ''
  categoryItems.forEach((item, index) => {
    category += '<div class="container-right-category-item">'
    category += '<div class="container-right-category-item-title">' + item.categoryName + '</div>'
    category += '<div class="container-right-category-item-content">'
	category += '<div class="container-right-category-item-content-all-wrap">'
    category += '<div class="container-right-category-item-content-all" category="' + item.category + '">'

	if(index == 0){
		category += '<input class="container-right-category-item-content-all-input-sport" type="checkbox" checked="checked" />'
		category += '<span class="container-right-category-item-content-all-text">全选</span>'
		category += '<div class="container-right-category-item-content-all-cover container-right-category-item-content-all-cover-sport" ></div>'
	}else if(index == 1){
		category += '<input class="container-right-category-item-content-all-input-esport" type="checkbox" checked="checked" />'
		category += '<span class="container-right-category-item-content-all-text">全选</span>'
		category += '<div class="container-right-category-item-content-all-cover container-right-category-item-content-all-cover-esport" ></div>'
	}
		category += '</div>'
		category += '</div>'
		category += '<div class="container-right-category-item-content-body">'
    item.items.forEach((tmpItem, tmpIndex) => {
      if ('sport' === item.category) {
        sport.push(tmpItem.key)
		category += '<div class="container-right-category-item-content-body-item container-right-category-item-content-body-item-sport container-right-category-item-content-body-item-active" category="' + item.category + '" key="' + tmpItem.key + '">'
		category += '<input type="checkbox" checked=' + tmpItem.checked + ' id="checkbox_category_' + (index + 1) + '_' + (tmpIndex + 1) + '" class="container-right-category-item-content-body-item-checkbox container-checkbox" />'
		category += '<label for="checkbox_category_' + (index + 1) + '_' + (tmpIndex + 1) + '" class="checkbox container-right-category-item-content-body-item-label1"></label>'
		category += '<label class="container-right-category-item-content-body-item-label2 container-right-category-item-content-body-item-label2-active">' + tmpItem.title + '</label>'
		category += '</div>'
      } else if ('esport' === item.category) {
        esport.push(tmpItem.key)
		category += '<div class="container-right-category-item-content-body-item container-right-category-item-content-body-item-esport container-right-category-item-content-body-item-active" category="' + item.category + '" key="' + tmpItem.key + '">'
		category += '<input type="checkbox" checked=' + tmpItem.checked + ' id="checkbox_category_' + (index + 1) + '_' + (tmpIndex + 1) + '" class="container-right-category-item-content-body-item-checkbox container-checkbox" />'
		category += '<label for="checkbox_category_' + (index + 1) + '_' + (tmpIndex + 1) + '" class="checkbox container-right-category-item-content-body-item-label1"></label>'
		category += '<label class="container-right-category-item-content-body-item-label2 container-right-category-item-content-body-item-label2-active">' + tmpItem.title + '</label>'
		category += '</div>'
      }

    })
    category += '</div>'
    category += '</div>'
    category += '</div>'
  })
  category += '<a class="logout-button" href="http://www.youdao.love/app1/logout/">退出</a>'
  $('.container-right-category').html(category)

  $('.container-right-category-item-content-all-cover-sport').off().click(function(){
  	categorySelectAll('sport')
  })
  $('.container-right-category-item-content-all-cover-esport').off().click(function(){
  	categorySelectAll('esport')
  })

	

}

function loadTableColumn() {
  let tableColumn = ''
  if ('valuebeyonddata' !== dataCode) {
    tableColumn += '<div class="container-left-body-title-profit container-left-body-profit">利润</div>'
  }
  tableColumn += '<div class="container-left-body-title-platform container-left-body-platform">参与平台</div>'
  tableColumn += '<div class="container-left-body-title-time container-left-body-time">开赛时间</div>'
  tableColumn += '<div class="container-left-body-title-project container-left-body-project">项目</div>'
  tableColumn += '<div class="container-left-body-title-position container-left-body-position">套利盘口</div>'
  tableColumn += '<div class="container-left-body-title-price container-left-body-price">赔率</div>'
  if ('valuebeyonddata' === dataCode) {
    tableColumn += '<div class="container-left-body-title-price container-left-body-overvalueRate">超值率</div>'
  }
  $('.container-left-body-title').html(tableColumn)
  loadGrid([])
}

function loadGrid(items) {
  items = items || gridData

  let grid = ''
  items.forEach(item => {
    grid += '<div class="container-left-body-content-item">'
    if ('valuebeyonddata' !== dataCode) {
      grid += '<div class="container-left-body-content-item-profit container-left-body-profit">'
      grid += '<div class="container-left-body-content-item-profit-item">'
      grid += '<div class="container-left-body-content-item-profit-item-ratio">'
      grid += '<span class="container-left-body-content-item-profit-item-ratio-number">' + item.profit.ratio + '</span>'
      grid += '<span class="container-left-body-content-item-profit-item-ratio-unit">%</span>'
      grid += '</div>'
      grid += '<div class="container-left-body-content-item-profit-item-timer">' + item.profit.timer + '</div>'
      grid += '<div class="container-left-body-content-item-profit-item-icon"></div>'
      grid += '</div>'
      grid += '</div>'
    }
    grid += '<div class="container-left-body-content-item-platform container-left-body-platform">'
    item.platform.forEach(platformItem => {
      grid += '<div class="container-left-body-content-item-platform-item">'
      grid += '<div class="container-left-body-content-item-platform-item-up">' + platformItem.platformName + '</div>'
      grid += '<div class="container-left-body-content-item-platform-item-down">' + platformItem.categoryName + '</div>'
      grid += '</div>'
    })
    grid += '</div>'
    grid += '<div class="container-left-body-content-item-time container-left-body-time">'
    item.timer.forEach(timerItem => {
      grid += '<div class="container-left-body-content-item-time-item">'
      grid += '<div class="container-left-body-content-item-time-item-up">' + timerItem.date + '</div>'
      grid += '<div class="container-left-body-content-item-time-item-down">' + timerItem.time + '</div>'
      grid += '</div>'
    })
    grid += '</div>'
    grid += '<div class="container-left-body-content-item-project container-left-body-project">'
    item.project.forEach(projectItem => {
      grid += '<div class="container-left-body-content-item-project-item">'
      grid += '<div class="container-left-body-content-item-project-item-up">' + projectItem.game + '</div>'
      grid += '<div class="container-left-body-content-item-project-item-down">' + projectItem.team + '</div>'
      grid += '</div>'
    })
    grid += '</div>'
    grid += '<div class="container-left-body-content-item-position container-left-body-position">'
    item.position.forEach(positionItem => {
      grid += '<div class="container-left-body-content-item-position-item">'
      grid += '<div class="container-left-body-content-item-position-item-icon"></div>'
      grid += '<div class="container-left-body-content-item-position-item-text">' + positionItem + '</div>'
      grid += '</div>'
    })
    grid += '</div>'
    grid += '<div class="container-left-body-content-item-price container-left-body-price">'
    item.odds.forEach(priceItem => {
      grid += '<div class="container-left-body-content-item-price-item">' + priceItem + '</div>'
    })
    grid += '</div>'
    if ('valuebeyonddata' === dataCode) {
      grid += '<div class="container-left-body-content-item-overvalueRate container-left-body-overvalueRate">'
      item.overvalueRate.forEach(overvalueRateItem => {
        grid += '<div class="container-left-body-content-item-overvalueRate-item">' + overvalueRateItem + '</div>'
      })
      grid += '</div>'
    }
    grid += '</div>'
  })
  $('.container-left-body-content').html(grid)
}
// 刷新函数
var refreshLimit = 0
function refresh() {
	if(refreshLimit<=0){
		getData("current")
		refreshLimit = 5
		$(".container-left-head-refresh-content-body-num").html(refreshLimit)
		$(".container-left-head-refresh-content").addClass("container-left-head-refresh-content-disabled")
		let timer = setInterval(function () {
			if(refreshLimit>1){
				refreshLimit--
				$(".container-left-head-refresh-content-body-num").html(refreshLimit)
			}else{
				refreshLimit = 0
				$(".container-left-head-refresh-content-body-num").html("")
				$(".container-left-head-refresh-content").removeClass("container-left-head-refresh-content-disabled")
				clearInterval(timer)
			}
		
		}, 1000)
	}

}

// 自动刷新
function AutoRefresh(e) {

}

// 设置自动刷新时长
function AutoRefreshTimes(e) {
  console.log(e);


}

/*
$(".container-left-head-refresh-content-body-title").click(function(){

})
*/



// 字符串中英文替换工具函数
function strLanguageConvert(str,targetLanguage){
	let translations = {
		    "188Bet": "皇冠",  
            "Pinnacle": "平博",  
            "BetVictor": "韦德[威廉]",  
            "SboBet": "利记",  
            "YSB": "易胜博",  
            "12Bet": "沙巴",
			"12​Bet": "沙巴",
            "V​Bet": "NewBB 体育",
            "1xBet": "1xBet",
            "Nextbet": "大发体育",  
            "GG​Bet": "GGBet",  
            "Tempo​Bet": "天宝博",
            "Counter-Strike": "反恐精英",  
            "Dota": "刀塔2",  
            "King of Glory": "王者荣耀",  
            "League of Legends": "英雄联盟",  
            "1(1-2)": "主胜（无平局）",  
            "2(1-2)": "客胜（无平局）",  
            "1 / DNB": "主胜（平局退款）",  
            "2 / DNB": "客胜（平局退款）",  
            "1X": "主胜或平局",  
            "X2": "平局或客胜",  
            "X": "平局",  
            "Booking": "罚牌",  
            "Win: 是 in overtime": "比赛结果决定于加时赛",  
            "第1 队": "主队",  
            "第2 队": "客队",  
            "tower": "推塔数",  
            "second yellow for one player as red": "球队罚牌数",    
            "2和大于": "客胜且客队进球大于",  
            "2和小于": "客胜且客队进球小于",  
            "加时": "含加时赛果",  
            "Roshan": "肉山",  
            "[race to 7 regular time]": "[率先取得第7分]",  
            "[race to 5 regular time]": "[率先取得第5分]",  
            "qualify": "晋级",  
            "1和1": "主胜且主队取得",  
            "1和2": "主胜且客队取得",  
            "2和2": "客胜且客队取得",  
            "2和1": "客胜且主队取得",  
            "第2 0 失球": "客队0失球",  
            "第1 0 失球": "主队0失球",  
            "击杀": "击杀数",  
            "2 - win": "客胜",  
            "1 – win": "主胜",
            "[race to 20 regular time]": "率先取得20分",  
            "[race to 15 regular time]": "率先取得15分",  
            "[race to 10 regular time]": "率先取得10分",  
            "[race to 25 regular time]": "率先取得25分",  
            "dragon": "小龙",  
            "roshan ordinal": "肉山",  
            "第1 时间段": "第一节",  
            "5 局": "前5局",  
            "第2 时间段": "第二节",  
			"第1 张地图": "地图1",  
            "第2 张地图": "地图2",  
            "第3 张地图": "地图3",
			 "让 1 队": "主队",
			"让 2 队": "客队"

    }
	let keys = Object.keys(translations)
	let values = Object.values(translations)
	let result = str

	
	if(targetLanguage == 'ZH'){
		let indexs = []
		
		for(let i=0;i<keys.length;i++){
			if(result){
				if(result.includes(keys[i]) || result==keys[i]){
					indexs.push(i)
				}
			}

		}
		if(indexs.length>0){
			for(let i=0;i<indexs.length;i++){
				result = result.replace(new RegExp(keys[indexs[i]],'g'), values[indexs[i]]);
				//result = result.replaceAll(keys[indexs[i]], values[indexs[i]]);
				if(i == indexs.length-1){
					
					return strReplace(result)
				}
			}
			
		}else{
			
			return strReplace(result)
		}
	}else if(targetLanguage == 'EN'){
		let indexs = []
		for(let i=0;i<values.length;i++){
			if(result){
				if(result.includes(values[i]) || result==values[i]){
					indexs.push(i)
				}
			}
			
		}
		if(indexs.length>0){
			for(let i=0;i<indexs.length;i++){
				result = result.replace(new RegExp(values[indexs[i]],'g'), keys[indexs[i]]);
				//result = result.replaceAll(values[indexs[i]], keys[indexs[i]]);
				if(i == indexs.length-1){
					return strReplace(result)
				}
			}
		}else{
			return strReplace(result)
		}
	}
}

function strReplace(result){
		
	result = result.replace(new RegExp('第1 队','g'), '主队');
	result = result.replace(new RegExp('让 1 队','g'), '主队');
	result = result.replace(new RegExp('第2 队','g'), '客队');
	result = result.replace(new RegExp('让 2 队','g'), '客队');
	result = result.replace(new RegExp('tower','g'), '推塔数');
	return result
}
// 字符串中英文筛选过滤工具函数
function strLanguageFilterate(str,targetLanguage){
	if(str==null || str==undefined){
		return ""
	}
	// 遍历所有的[]，获取它们的下标,按数组存放[[左括号索引、右括号索引],[]...]
	let bracketIndexs = []
	let leftBracketIndex = null
	let rightBracketIndex = null
	
	for(let i=0;i<str.length;i++){
		if(str[i] == '['){
			leftBracketIndex = i
		}
		if(str[i] == ']'){
			rightBracketIndex = i
		}

		if(leftBracketIndex!=null && rightBracketIndex!=null ){
			let tempArr = []
			tempArr.push(leftBracketIndex,rightBracketIndex)
			bracketIndexs.push(tempArr)
			leftBracketIndex = null
			rightBracketIndex = null
		}
	}
	//console.log("方括号索引数组：",bracketIndexs)
	if(!bracketIndexs || bracketIndexs.length<=0){
		return str
	}
	
	let dataArr = []
	if(targetLanguage == 'ZH'){// 中文
		let result = ""
		for(let i=0;i<bracketIndexs.length;i++){
			let leftBracketIndex = bracketIndexs[i][0]
			let rightBracketIndex = bracketIndexs[i][1]
			let dataStr = str.substring(leftBracketIndex+1,rightBracketIndex)
			let isOnlyWordAndNumber = validOnlyWordAndNumber(dataStr)
			if(!isOnlyWordAndNumber){
				dataArr.push(dataStr)
			}
			
		}
		//console.log("数据列表：",dataArr)
		for(let i=0;i<dataArr.length;i++){
			result += dataArr[i]
			if(dataArr.length>1 && i<=dataArr.length-2){
				result += "-"
			}
		}
		return result
	}else if(targetLanguage == 'EN'){// 英文
		let result = ""
		let startIndex = 0
		for(let i=0;i<bracketIndexs.length;i++){
			let leftBracketIndex = bracketIndexs[i][0]
			let rightBracketIndex = bracketIndexs[i][1]
			let dataStr = str.substring(startIndex,leftBracketIndex)
			dataArr.push(dataStr)
			startIndex = rightBracketIndex+1
			if(i == bracketIndexs.length-1 && rightBracketIndex<str.length-1){
				let dataStr = str.substring(rightBracketIndex+1,str.length-1)
				dataArr.push(dataStr)
			}
		}
		//console.log("数据列表：",dataArr)
		dataArr.forEach(item=>{
			result+=item
		})
		return result
	}
	


}

function validOnlyWordAndNumber(str) {
  const reg = new RegExp("^[a-zA-z0-9]+$")
  return reg.test(str)
}

function validHasDigit(str) {
  const reg = new RegExp("\\d")
  return reg.test(str);
}
