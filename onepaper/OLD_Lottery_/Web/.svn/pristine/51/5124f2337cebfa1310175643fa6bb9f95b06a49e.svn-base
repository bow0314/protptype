$(document).ready(function(){
    /*--- 判斷是否為Ie8 ---*/
    var ieVersion=parseFloat($.browser.version);    //抓取瀏覽器版本
    var nowDay=new Date().getDay();
    var arryLottery = ["Power","Power","Big","Dafu","Power","Big","Dafu"];
    var nowLottery = arryLottery[nowDay];
    var lotteryCount;
    $.getJSON("http://220.128.150.80:17180/lottery/rest/new",function(data){
        var thisData = data;
        $("#text1>span").html(thisData[nowLottery].LottoName);
        lotteryCount = thisData[nowLottery].WinMoneyNonFormat;
        CountDownTimer(lotteryCount, 'number');
    });
    // $.ajax({
    //     url: "http://220.128.150.80:17180/lottery/rest/new",
    //     type:"Get",
    //     data: "{}",
    //     dataType:"json",
    //     cache: false,
    //     success: function(data){
    //         var thisData = data;
    //         $("#text1>span").html(thisData[nowLottery].LottoName);
    //         lotteryCount = thisData[nowLottery].WinMoneyNonFormat;
    //         console.log(lotteryCount);
    //         CountDownTimer(lotteryCount, 'number');
    //     },
    //     error:function(xhr, status, errorThrown) {
    //         console.log('@Error: '+errorThrown);
    //         console.log('@Status: '+status);
    //         console.log('@Status Text: '+xhr.statusText);
    //     }
    // });
    function CountDownTimer(dt, id)
    {
        var end = dt;               //此頭獎預估獎金
        var arry = end.split("");   //轉矩陣
        var num = end.length;       //數量
        var now = 0;                //現在跑的次數
        var size = 800;             
        var time = num*size;        //總次數
        var speed = 5;             //速度
        var timer;                  //計時器
        function showRemaining() {
          
            if(now<time){
                var this_html = ''; 
                if(num<10){
                    for(var i =0;i<10-num;i++){
                        this_html += '<span>0</span>';
                    }
                }
                var n = Math.floor(time/now)-1;
                for(var i =0;i<num;i++){
                    var random = Math.floor(Math.random() * (10 - 1)) + 0;  
                    if(now>size){
                        if(i<n){
                            this_html += '<span>' + random +'</span>';
                        }else{
                            this_html += '<span>' + arry[i] +'</span>';
                        }
                    }else{
                        this_html += '<span>' + random +'</span>';
                    }          
                }
                document.getElementById(id).innerHTML = this_html;
                if(ieVersion==8){
                    $('#number span:nth-child(3n+1)').css({'margin-right':'14px'});
                }
                
                now++;
                if(now>size && n==1){
                    speed =200;
                }else{
                    speed +=10;
                }
                timer = setInterval(showRemaining, speed);
            }else{
                return;
            }
        }
        timer = setTimeout(showRemaining, speed);
}
});


