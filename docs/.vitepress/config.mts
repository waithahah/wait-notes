import { defineConfig } from 'vitepress'
import fs from 'fs'
import path from 'path'

function cleanPath(p: string) {
  return p.replace(/\\/g, '/')
}

function getNotesSidebar() {
  const notesDir = path.resolve(__dirname, '../notes')
  
  function scan(dir: string, baseRoute: string) {
    if (!fs.existsSync(dir)) return []
    const items = fs.readdirSync(dir)
    let result: any[] = []
    
    items.forEach(item => {
      const fullPath = path.join(dir, item)
      const stat = fs.statSync(fullPath)
      const route = baseRoute + '/' + item
      
      if (stat.isDirectory()) {
        const subItems = scan(fullPath, route)
        if (subItems.length > 0) {
          result.push({
            text: item,
            collapsed: true,
            items: subItems
          })
        }
      } else if (item.endsWith('.md')) {
        const title = item.replace(/\.md$/, '')
        const link = route.replace(/\.md$/, '')
        result.push({
          text: title,
          link: cleanPath(link)
        })
      }
    })
    return result
  }
  
  return scan(notesDir, '/notes')
}

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "Wait",
  description: "记录思想与技术的轻量极速笔记空间",
  ignoreDeadLinks: true,
  head: [
    ['link', { rel: 'icon', href: '/logo.png' }]
  ],
  themeConfig: {
    logo: '/logo.png',
    search: {
      provider: 'local',
      options: {
        locales: {
          root: {
            translations: {
              button: {
                buttonText: '搜索...',
                buttonAriaLabel: '搜索文档'
              },
              modal: {
                noResultsText: '未找到相关笔记文档',
                resetButtonTitle: '清除搜索条件',
                footer: {
                  selectText: '选择',
                  navigateText: '切换',
                  closeText: '关闭'
                }
              }
            }
          }
        }
      }
    },

    nav: [
      { text: '首页', link: '/' },
      { text: '笔记', link: '/notes/README' },
      { text: '项目', link: '/notes/项目/qiko+/3.Qiko+部署文档' },
      { text: '归档', link: '/notes/导航' },
      { text: '关于', link: '/notes/README' }
    ],

    sidebar: {
      '/notes/': getNotesSidebar(),
      '/': getNotesSidebar()
    },

    socialLinks: [
      { icon: 'github', link: 'https://github.com/waithahah' }
    ],

    footer: {
      message: 'Released under the MIT License.',
      copyright: 'Copyright © 2026-present waithahah'
    }
  }
})
