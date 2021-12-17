# iidx_misc
弐寺関係のツールなど

# 公式サイトからjsでスクレイピングする方法
BISTROVERの11，12を全探索してdb11,db12に配列として保存してから、json文字列として出力。  
Chromeのデバッガ(F12)でイーアミュサイトを開いてからやると楽。  

各レベルのページは50ずつ開けるようになっている。  
iidx28時点でSP11=465譜面, SP12=410譜面となっており、この数字に合わせてfor文を作り込んでいるので注意。
```
function gethtml(url){
    let parser = new DOMParser();
    var req= new XMLHttpRequest();
    req.open('GET', url, false);
    req.send(null); 
    let doc = parser.parseFromString(req.responseText, "text/html");
    return(doc);
}

function parse_song(song){
    tds=song.getElementsByTagName('td');
    let title = tds[0].innerText;
    let difficulty = tds[1].innerText;
    let sctmp = tds[3].innerText;
    let score = sctmp.substr(0,sctmp.indexOf("("));
    let lamp_url=tds[4].getElementsByTagName("img")[0].getAttribute("src");
    let lamp=lamp_url.substr(lamp_url.length-5,1);
    let lt=["NO PLAY","FAILED","ASSIST CLEAR","EASY CLEAR","CLEAR","HARD CLEAR","EX HARD CLEAR","FULLCOMBO CLEAR"]
    //let ret = [title,difficulty,score,lt[+lamp]];
    let ret = [title,difficulty,score,lamp];
    return(ret);
}

let db12=[];let db11=[]
for (let lv=0;lv<2;lv++){
    for (let i=0;i<10-lv;i++){
        let ofst=50*i;
        let level=10+lv;
        var url = "https://p.eagate.573.jp/game/2dx/28/djdata/music/difficulty.html?difficult="+level.toString()+"&style=0&disp=1&offset="+ofst.toString();
        a = gethtml(url);
        tmp=a.getElementById("base-inner");
        div=tmp.getElementsByTagName("div")[8];
        songs=div.getElementsByTagName("tr");
        for (let i=2;i<songs.length;i++){
            if (lv==1){
                db12.push(parse_song(songs[i]));
            }else{
                db11.push(parse_song(songs[i]));
            }
        }
    }
} 

let out="[";
for (const x of db12){
    out+="{";
    out+='"title":'+'"'+x[0].replace('”','\"')+'",';
    out+='"difficulty":'+'"'+x[1].toLowerCase()+'",';
    out+='"clear":'+x[3]+',';
    out+='"score":'+x[2]+'';
    out+="},";
}
for (const x of db11){
    out+="{";
    out+='"title":'+'"'+x[0].replace('”','\"')+'",';
    out+='"difficulty":'+'"'+x[1].toLowerCase()+'",';
    out+='"clear":'+x[3]+',';
    out+='"score":'+x[2]+'';
    out+="},";
}
out+="]";
```
