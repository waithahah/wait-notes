## 支持流式响应
// 适量大一些
client_max_body_size ${NGINX_CLIENT_MAX_BODY_SIZE};  
// 关闭缓存 
proxy_buffering off;