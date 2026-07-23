cd /data/polynex/face_cluster/
curl --location --request POST 'http://36.248.221.206:10111/clustering/process' --header 'Content-Type: application/json' --data @data.json


共 128 

没聚类 10 

聚类 8 组
0 45
1 29
2 16
3 16
4 3
5 4
6 2
7 2

未知
1



中检服务器删除缓存并重启
cd /data/.mycluster/ && rm -r 10111/* && cd /data/polynex/face_cluster/cluster/ && sudo lsof -ti:10111 | xargs -r kill -9 &&  nohup bash run.sh 2>&1 &

cd /data/tianq/nex_fusion/api/core/face_cluster && bash start_restart_cluster.sh
curl -X POST http://172.16.0.4:8181/restart_face_cluster

20251105更新
启动
bash /data/wwtest/xujl/polynex_cluster/mycluster/start_mycluster10111.sh
停止
bash /data/wwtest/xujl/polynex_cluster/mycluster/stop_mycluster10111.sh
查看日志
tail -f /data/log/$(date +%Y%m%d)/myclusterface10111.log