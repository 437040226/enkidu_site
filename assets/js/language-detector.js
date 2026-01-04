(function() {
    // 检查是否已经运行过，避免无限循环重定向
    if (sessionStorage.getItem('languageDetected')) {
        return;
    }

    // 从 <html> 标签的 lang 属性获取当前页面的语言
    const currentLang = document.documentElement.lang || 'en';
    
    // 从浏览器获取用户首选语言列表
    const browserLanguages = navigator.languages || [navigator.language];
    
    // 定义我们网站支持的语言
    const supportedLanguages = ['zh-CN', 'en'];

    let detectedLang = null;

    // 遍历浏览器语言列表，找到第一个我们支持的语言
    for (let i = 0; i < browserLanguages.length; i++) {
        const lang = browserLanguages[i];
        // 规范化语言代码，例如 'zh-CN' -> 'zh-cn', 'en-US' -> 'en'
        const normalizedLang = lang.toLowerCase().split('-')[0];

        if (normalizedLang === 'zh') {
            detectedLang = 'zh-CN';
            break;
        } else if (normalizedLang === 'en') {
            detectedLang = 'en';
            break;
        }
    }

    // 如果没有在浏览器语言中找到支持的语言，则使用默认语言
    if (!detectedLang) {
        detectedLang = 'en'; // 默认使用英文
    }

    // 获取当前路径并清理语言前缀
    const targetPath = window.location.pathname;
    let cleanPath = targetPath;
    
    // 移除语言前缀，但保留路径结构
    const langPrefixRegex = /^\/(zh-cn|en)(\/|$)/i;
    if (langPrefixRegex.test(targetPath)) {
        cleanPath = targetPath.replace(langPrefixRegex, '/');
    }
    
    // 构建目标URL
    let targetUrl;
    if (cleanPath === '/') {
        targetUrl = `/${detectedLang.toLowerCase()}/`;
    } else {
        targetUrl = `/${detectedLang.toLowerCase()}${cleanPath}`;
    }

    // 如果检测到的语言与当前页面的语言不一致，则进行重定向
    if (detectedLang && detectedLang !== currentLang) {
        // 标记为已检测，防止重定向循环
        sessionStorage.setItem('languageDetected', 'true');
        
        // 执行重定向
        window.location.href = targetUrl;
    } else {
        // 如果语言匹配，也标记为已检测
        sessionStorage.setItem('languageDetected', 'true');
    }
})();