const fs = require('fs');
const path = require('path');

// 定义输入和输出文件路径
const enFilePath = path.join(__dirname, 'public', 'algolia.json');
const zhFilePath = path.join(__dirname, 'public', 'zh-cn', 'algolia.json');
const mergedFilePath = path.join(__dirname, 'public', 'algolia.json');

try {
  // 读取英文索引文件
  const enData = JSON.parse(fs.readFileSync(enFilePath, 'utf8'));
  
  // 读取中文索引文件
  const zhData = JSON.parse(fs.readFileSync(zhFilePath, 'utf8'));
  
  // 合并两个数组
  const mergedData = [...enData, ...zhData];
  
  // 将合并后的数据写入新文件
  fs.writeFileSync(mergedFilePath, JSON.stringify(mergedData, null, 2));
  
  console.log(`Successfully merged ${enData.length} English records and ${zhData.length} Chinese records into ${mergedFilePath}`);

} catch (error) {
  console.error('Error merging Algolia files:', error.message);
  process.exit(1); // 以错误码退出，中断后续流程
}