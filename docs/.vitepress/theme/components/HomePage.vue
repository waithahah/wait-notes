<template>
  <div class="custom-home-wrapper">
    <!-- Ambient Background Glow & Stars -->
    <div class="ambient-glow"></div>
    <div class="stars-particle"></div>

    <div class="home-container">
      <!-- 1. Floating Pill Header Bar -->
      <header class="top-nav-pill">
        <div class="nav-left">
          <div class="logo-box">
            <img src="/logo.png" alt="Wait Notes Logo" class="logo-img" />
          </div>
          <span class="site-title">Wait</span>
        </div>

        <!-- Fuzzy Search Bar -->
        <div class="nav-search-container">
          <div class="search-input-wrapper">
            <svg class="search-icon" viewBox="0 0 24 24" width="16" height="16">
              <path fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/>
            </svg>
            <input 
              ref="searchInputRef"
              type="text" 
              v-model="searchQuery" 
              placeholder="搜索..." 
              @focus="isSearchOpen = true"
              @blur="closeSearch"
            />
          </div>

          <!-- Search Results Dropdown -->
          <div class="search-dropdown" v-if="isSearchOpen && searchQuery.trim()">
            <div class="dropdown-header" v-if="filteredNotes.length">
              找到 {{ filteredNotes.length }} 篇匹配笔记
            </div>
            <div class="dropdown-empty" v-else>
              未找到与 "{{ searchQuery }}" 相关的笔记文档
            </div>

            <div class="dropdown-list">
              <a 
                v-for="item in filteredNotes" 
                :key="item.path" 
                :href="item.path" 
                class="dropdown-item"
              >
                <div class="item-title-row">
                  <span class="item-category-tag">{{ item.category }}</span>
                  <span class="item-title">{{ item.title }}</span>
                </div>
                <div class="item-path">{{ item.fullPath }}</div>
              </a>
            </div>
          </div>
        </div>

        <nav class="nav-center">
          <a href="/" class="nav-item active">首页</a>
          <a href="/notes/README" class="nav-item">笔记</a>
          <a href="/notes/项目/qiko+/3.Qiko+部署文档" class="nav-item">项目</a>
          <a href="/notes/导航" class="nav-item">归档</a>
          <a href="/notes/README" class="nav-item">关于</a>
        </nav>

        <div class="nav-right">
          <button 
            class="theme-switch-btn" 
            :class="{ 'is-dark': isDark }" 
            @click="toggleTheme" 
            aria-label="切换深色/浅色主题" 
            title="切换主题"
          >
            <span class="switch-thumb">
              <svg v-if="!isDark" class="sun-icon" viewBox="0 0 24 24" width="12" height="12">
                <circle cx="12" cy="12" r="4" fill="currentColor"/>
                <path stroke="currentColor" stroke-width="2" stroke-linecap="round" d="M12 2v2m0 16v2M4.93 4.93l1.41 1.41m11.32 11.32l1.41 1.41M2 12h2m16 0h2M4.93 19.07l1.41-1.41m11.32-11.32l1.41-1.41"/>
              </svg>
              <svg v-else class="moon-icon" viewBox="0 0 24 24" width="12" height="12">
                <path fill="currentColor" d="M12.3 22A10 10 0 0 0 22 12.3a.5.5 0 0 0-.54-.53A9 9 0 0 1 12.23 2.54a.5.5 0 0 0-.53-.54A10 10 0 0 0 12.3 22Z"/>
              </svg>
            </span>
          </button>
          <span class="nav-divider">|</span>
          <a href="https://github.com/waithahah" target="_blank" class="github-icon-link" title="GitHub Profile">
            <svg class="github-svg" viewBox="0 0 24 24" width="20" height="20">
              <path fill="currentColor" d="M12 2A10 10 0 0 0 2 12c0 4.42 2.87 8.17 6.84 9.5.5.08.66-.23.66-.5v-1.69c-2.77.6-3.36-1.34-3.36-1.34-.46-1.16-1.11-1.47-1.11-1.47-.91-.62.07-.6.07-.6 1 .07 1.53 1.03 1.53 1.03.87 1.52 2.34 1.07 2.91.83.1-.65.35-1.09.63-1.34-2.22-.25-4.55-1.11-4.55-4.92 0-1.11.38-2 1.03-2.71-.1-.25-.45-1.29.1-2.64 0 0 .84-.27 2.75 1.02.79-.22 1.65-.33 2.5-.33.85 0 1.71.11 2.5.33 1.91-1.29 2.75-1.02 2.75-1.02.55 1.35.2 2.39.1 2.64.65.71 1.03 1.6 1.03 2.71 0 3.82-2.34 4.66-4.57 4.91.36.31.69.92.69 1.85V21c0 .27.16.59.67.5C19.14 20.16 22 16.42 22 12A10 10 0 0 0 12 2Z"/>
            </svg>
          </a>
        </div>
      </header>

      <!-- 2. Hero Section (Left Content + Right 3D Stage) -->
      <section class="hero-section">
        <!-- Hero Left -->
        <div class="hero-left">
          <h1 class="hero-title">
            记录技术感悟，<br />
            沉淀<span class="gradient-text">知识与灵感</span>
          </h1>

          <p class="hero-subtitle">个人数字花园 · 笔记空间 · 项目文档中心</p>

          <p class="hero-desc">
            探索技术与思考的交汇点，记录学习的轨迹，分享实践的经验，让知识在连接中生长。
          </p>

          <div class="hero-actions">
            <a href="/notes/README" class="btn-primary">
              <span class="btn-icon">💬</span>
              <span>开始阅读</span>
              <span class="arrow">➔</span>
            </a>
            <a href="https://github.com/waithahah" target="_blank" class="btn-secondary">
              <svg class="github-svg" viewBox="0 0 24 24" width="18" height="18">
                <path fill="currentColor" d="M12 2A10 10 0 0 0 2 12c0 4.42 2.87 8.17 6.84 9.5.5.08.66-.23.66-.5v-1.69c-2.77.6-3.36-1.34-3.36-1.34-.46-1.16-1.11-1.47-1.11-1.47-.91-.62.07-.6.07-.6 1 .07 1.53 1.03 1.53 1.03.87 1.52 2.34 1.07 2.91.83.1-.65.35-1.09.63-1.34-2.22-.25-4.55-1.11-4.55-4.92 0-1.11.38-2 1.03-2.71-.1-.25-.45-1.29.1-2.64 0 0 .84-.27 2.75 1.02.79-.22 1.65-.33 2.5-.33 1.91-1.29 2.75-1.02 2.75-1.02.55 1.35.2 2.39.1 2.64.65.71 1.03 1.6 1.03 2.71 0 3.82-2.34 4.66-4.57 4.91.36.31.69.92.69 1.85V21c0 .27.16.59.67.5C19.14 20.16 22 16.42 22 12A10 10 0 0 0 12 2Z"/>
              </svg>
              <span>GitHub @waithahah</span>
            </a>
          </div>

          <div class="hero-badges">
            <span class="badge-pill"><span class="pill-icon">🎯</span> 专注记录</span>
            <span class="badge-pill"><span class="pill-icon">🔄</span> 持续沉淀</span>
            <span class="badge-pill"><span class="pill-icon">🔀</span> 开放分享</span>
          </div>
        </div>

        <!-- Hero Right 3D Stage & Code Box -->
        <div class="hero-right">
          <div class="stage-container">
            <!-- Floating Elements -->
            <div class="floating-card float-code-icon">
              <span class="code-symbol">&lt;/&gt;</span>
            </div>

            <div class="floating-card float-editor">
              <div class="pencil-icon">✏️</div>
              <div class="lines-placeholder">
                <div class="line line-short"></div>
                <div class="line line-long"></div>
              </div>
            </div>

            <div class="floating-card float-chart">
              <svg viewBox="0 0 80 40" class="mini-chart">
                <path d="M5 30 Q 25 35, 45 15 T 75 10" fill="none" stroke="#8B5CF6" stroke-width="3" stroke-linecap="round" />
                <circle cx="75" cy="10" r="4" fill="#8B5CF6" />
              </svg>
            </div>

            <!-- Main Code Window -->
            <div class="code-window">
              <div class="window-header">
                <div class="window-dots">
                  <span class="dot red"></span>
                  <span class="dot yellow"></span>
                  <span class="dot green"></span>
                </div>
              </div>
              <div class="code-content">
                <p class="code-comment">// Welcome to Wait Notes</p>
                <br />
                <p><span class="kwd">const</span> <span class="var">waitNotes</span> = {</p>
                <p class="indent"><span class="key">ideas</span>: <span class="str">"记录灵感"</span>,</p>
                <p class="indent"><span class="key">notes</span>: <span class="str">"沉淀知识"</span>,</p>
                <p class="indent"><span class="key">share</span>: <span class="str">"连接世界"</span></p>
                <p>}</p>
                <br />
                <p><span class="kwd">export default</span> <span class="var">waitNotes</span></p>
              </div>
            </div>

            <!-- 3D Pedestal Stage & Glowing Crystal Cube -->
            <div class="pedestal-stage">
              <div class="crystal-cube"></div>
              <div class="pedestal-disc disc-3"></div>
              <div class="pedestal-disc disc-2"></div>
              <div class="pedestal-disc disc-1"></div>
            </div>
          </div>
        </div>
      </section>

      <!-- 3. 5 Feature Cards Row -->
      <section class="feature-cards-row">
        <a href="/notes/学习/git/git" class="feature-card">
          <div class="card-icon-box bg-purple-1">
            <svg viewBox="0 0 24 24" width="24" height="24" fill="white">
              <path d="M12 3L1 9l11 6 9-4.91V17h2V9L12 3zm0 13.52L3.5 12 12 7.35 20.5 12 12 16.52zM3.5 14.85L12 19.5l8.5-4.65v2.3L12 21.8l-8.5-4.65v-2.3z"/>
            </svg>
          </div>
          <div class="card-body">
            <h3 class="card-title">技术沉淀</h3>
            <p class="card-desc">记录编程、思维、工程化等重要实践与思考笔记，打造系统化知识体系。</p>
          </div>
          <span class="card-arrow">➔</span>
        </a>

        <a href="/notes/vibecoding/claudecode" class="feature-card">
          <div class="card-icon-box bg-purple-2">
            <svg viewBox="0 0 24 24" width="24" height="24" fill="white">
              <path d="M3 17.25V21h3.75L17.81 9.94l-3.75-3.75L3 17.25zM20.71 7.04c.39-.39.39-1.02 0-1.41l-2.34-2.34c-.39-.39-1.02-.39-1.41 0l-1.83 1.83 3.75 3.75 1.83-1.83z"/>
            </svg>
          </div>
          <div class="card-body">
            <h3 class="card-title">日常随笔</h3>
            <p class="card-desc">散文式感悟随写，写前沿思考与生活点滴，保持热爱与好奇探索。</p>
          </div>
          <span class="card-arrow">➔</span>
        </a>

        <a href="/notes/项目/qiko+/3.Qiko+部署文档" class="feature-card">
          <div class="card-icon-box bg-pink-1">
            <svg viewBox="0 0 24 24" width="24" height="24" fill="white">
              <path d="M10 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V8c0-1.1-.9-2-2-2h-8l-2-2z"/>
            </svg>
          </div>
          <div class="card-body">
            <h3 class="card-title">项目文档</h3>
            <p class="card-desc">整理项目文档与开发经验，沉淀可复用的解决方案与抽象。</p>
          </div>
          <span class="card-arrow">➔</span>
        </a>

        <a href="/notes/vscode配置/配置" class="feature-card">
          <div class="card-icon-box bg-indigo-1">
            <svg viewBox="0 0 24 24" width="24" height="24" fill="white">
              <path d="M7 2v11h3v9l7-12h-4l4-8z"/>
            </svg>
          </div>
          <div class="card-body">
            <h3 class="card-title">效率工具</h3>
            <p class="card-desc">收集常用开发资源、模板和小技巧，提升创造力。</p>
          </div>
          <span class="card-arrow">➔</span>
        </a>

        <a href="/notes/临时/cozedify" class="feature-card">
          <div class="card-icon-box bg-violet-1">
            <svg viewBox="0 0 24 24" width="24" height="24" fill="white">
              <path d="M9 21c0 .55.45 1 1 1h4c.55 0 1-.45 1-1v-1H9v1zm3-19C8.14 2 5 5.14 5 9c0 2.38 1.19 4.47 3 5.74V17c0 .55.45 1 1 1h6c.55 0 1-.45 1-1v-2.26c1.81-1.27 3-3.36 3-5.74 0-3.86-3.14-7-7-7z"/>
            </svg>
          </div>
          <div class="card-body">
            <h3 class="card-title">灵感闪光</h3>
            <p class="card-desc">记录创新想法、可复用思路与技术碎片，让灵感随时可查。</p>
          </div>
          <span class="card-arrow">➔</span>
        </a>
      </section>

      <!-- 4. Bottom Two-Column Section (Latest Notes & Hot Projects) -->
      <section class="bottom-section-grid">
        <!-- Left: 最新笔记 -->
        <div class="section-column">
          <div class="column-header">
            <div class="header-left">
              <span class="header-icon">📰</span>
              <h2 class="column-title">最新笔记</h2>
            </div>
            <a href="/notes/README" class="more-link">查看全部 ➔</a>
          </div>

          <div class="notes-list">
            <a href="/notes/部署记录/bamboo/bamboo部署" class="note-item-card">
              <div class="note-thumb thumb-1">
                <div class="thumb-decor decor-cube"></div>
              </div>
              <div class="note-content">
                <h3 class="note-title">Bamboo 服务项目自动化部署指南</h3>
                <p class="note-summary">记录搭建过程中的关键实践、环境配置与部署经验。</p>
                <div class="note-meta">
                  <span class="meta-item">🕒 2024-05-18</span>
                  <span class="meta-dot">·</span>
                  <span class="meta-item">🏷️ 服务部署</span>
                </div>
              </div>
            </a>

            <a href="/notes/Python/1.python和java对比" class="note-item-card">
              <div class="note-thumb thumb-2">
                <div class="thumb-decor decor-ts"></div>
              </div>
              <div class="note-content">
                <h3 class="note-title">Python 与 Java 核心特性对比与深入解析</h3>
                <p class="note-summary">深入探索语法与运行机制原理与边界，掌握语言系统的力量。</p>
                <div class="note-meta">
                  <span class="meta-item">🕒 2024-05-10</span>
                  <span class="meta-dot">·</span>
                  <span class="meta-item">🏷️ Python</span>
                </div>
              </div>
            </a>
          </div>
        </div>

        <!-- Right: 热门项目 -->
        <div class="section-column">
          <div class="column-header">
            <div class="header-left">
              <span class="header-icon">🔮</span>
              <h2 class="column-title">热门项目</h2>
            </div>
            <a href="/notes/项目/qiko+/3.Qiko+部署文档" class="more-link">查看全部 ➔</a>
          </div>

          <div class="projects-list">
            <a href="/notes/项目/qiko+/3.Qiko+部署文档" class="project-item-card" style="text-decoration: none; color: inherit; display: block;">
              <div class="project-header">
                <div class="project-logo">
                  <img src="/logo.png" alt="Wait Notes Logo" class="project-logo-img" />
                </div>
                <div class="project-info">
                  <h3 class="project-name">Qiko+ 智能体平台</h3>
                  <p class="project-desc">一套功能强大的智能体与大模型服务平台，开箱即用，支持多模态及知识库部署。</p>
                </div>
              </div>

              <div class="project-tags">
                <span class="ptag">Python / Flask</span>
                <span class="ptag">智能体架构</span>
                <span class="ptag">MIT License</span>
              </div>

              <div class="project-stats">
                <span class="stat-item">⭐ 128</span>
                <span class="stat-item">🍴 32</span>
              </div>
            </a>
          </div>
        </div>
      </section>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'

const isDark = ref(false)
const searchQuery = ref('')
const isSearchOpen = ref(false)
const notesIndex = ref([])
const searchInputRef = ref(null)

const updateDark = () => {
  if (typeof document !== 'undefined') {
    isDark.value = document.documentElement.classList.contains('dark')
  }
}

const handleKeydown = (e) => {
  if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
    e.preventDefault()
    if (searchInputRef.value) {
      searchInputRef.value.focus()
    }
  }
}

onMounted(async () => {
  updateDark()
  try {
    const res = await fetch('/search-index.json')
    if (res.ok) {
      notesIndex.value = await res.json()
    }
  } catch (e) {
    console.error('Failed to load search index:', e)
  }

  if (typeof window !== 'undefined') {
    window.addEventListener('keydown', handleKeydown)
  }
})

onUnmounted(() => {
  if (typeof window !== 'undefined') {
    window.removeEventListener('keydown', handleKeydown)
  }
})

const filteredNotes = computed(() => {
  if (!searchQuery.value.trim()) return []
  const query = searchQuery.value.toLowerCase().trim()
  return notesIndex.value.filter(item => {
    return (
      item.title.toLowerCase().includes(query) ||
      item.category.toLowerCase().includes(query) ||
      item.fullPath.toLowerCase().includes(query)
    )
  }).slice(0, 10)
})

const closeSearch = () => {
  setTimeout(() => {
    isSearchOpen.value = false
  }, 200)
}

const toggleTheme = () => {
  if (typeof document !== 'undefined') {
    document.documentElement.classList.toggle('dark')
    updateDark()
  }
}
</script>

<style scoped>
/* 1:1 Design Replica Styling */

.custom-home-wrapper {
  min-height: 100vh;
  background: linear-gradient(180deg, #F5F1FD 0%, #EFEAFB 40%, #E7E0F8 100%);
  color: #1F1B2E;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  position: relative;
  overflow: hidden;
  padding-bottom: 60px;
}

.dark .custom-home-wrapper {
  background: linear-gradient(180deg, #0D0A1A 0%, #120E24 40%, #181330 100%);
  color: #F3F0FE;
}

/* Ambient Background Lights */
.ambient-glow {
  position: absolute;
  top: -200px;
  left: 50%;
  transform: translateX(-50%);
  width: 1200px;
  height: 700px;
  background: radial-gradient(circle, rgba(168, 85, 247, 0.25) 0%, rgba(124, 58, 237, 0.1) 45%, transparent 70%);
  pointer-events: none;
  filter: blur(90px);
}

.home-container {
  max-width: 1240px;
  margin: 0 auto;
  padding: 20px 24px;
  position: relative;
  z-index: 1;
}

/* 1. Floating Pill Header Nav Bar */
.top-nav-pill {
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: rgba(255, 255, 255, 0.85);
  backdrop-filter: blur(20px);
  border: 1px solid rgba(255, 255, 255, 0.6);
  border-radius: 999px;
  padding: 10px 24px;
  margin-bottom: 40px;
  box-shadow: 0 10px 30px rgba(124, 58, 237, 0.06);
}

.dark .top-nav-pill {
  background: rgba(24, 19, 48, 0.8);
  border-color: rgba(139, 92, 246, 0.2);
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
}

.nav-left {
  display: flex;
  align-items: center;
  gap: 12px;
}

.logo-box {
  width: 36px;
  height: 36px;
  border-radius: 10px;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #FFF;
  box-shadow: 0 4px 12px rgba(124, 58, 237, 0.2);
}

.logo-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.site-title {
  font-size: 1.15rem;
  font-weight: 700;
  color: #1F1B2E;
}

/* Fuzzy Search Bar Styling */
.nav-search-container {
  position: relative;
  margin-left: 24px;
  flex: 1;
  max-width: 280px;
}

.search-input-wrapper {
  display: flex;
  align-items: center;
  gap: 8px;
  background: transparent;
  border: 1px solid rgba(124, 58, 237, 0.15);
  border-radius: 999px;
  padding: 6px 14px;
  transition: all 0.25s ease;
}

.dark .search-input-wrapper {
  background: transparent;
  border-color: rgba(192, 132, 252, 0.2);
}

.search-input-wrapper:hover {
  border-color: rgba(124, 58, 237, 0.35);
  background: rgba(124, 58, 237, 0.03);
}

.search-input-wrapper:focus-within {
  border-color: #7C3AED;
  background: #FFFFFF;
  box-shadow: 0 4px 16px rgba(124, 58, 237, 0.15);
}

.dark .search-input-wrapper:focus-within {
  border-color: #C084FC;
  background: #181330;
  box-shadow: 0 4px 16px rgba(168, 85, 247, 0.25);
}

.search-icon {
  color: #8B5CF6;
  flex-shrink: 0;
}

.search-input-wrapper input {
  border: none;
  background: transparent;
  outline: none;
  font-size: 0.85rem;
  color: #1F1B2E;
  width: 100%;
}

.dark .search-input-wrapper input {
  color: #FFF;
}

.shortcut-kbd {
  font-family: monospace;
  font-size: 0.65rem;
  padding: 2px 6px;
  border-radius: 4px;
  background: rgba(124, 58, 237, 0.1);
  color: #7C3AED;
  border: 1px solid rgba(124, 58, 237, 0.2);
  flex-shrink: 0;
}

.dark .shortcut-kbd {
  background: rgba(192, 132, 252, 0.15);
  color: #C084FC;
  border-color: rgba(192, 132, 252, 0.3);
}

/* Dropdown list */
.search-dropdown {
  position: absolute;
  top: calc(100% + 10px);
  left: 0;
  width: 360px;
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(20px);
  border: 1px solid rgba(124, 58, 237, 0.2);
  border-radius: 16px;
  box-shadow: 0 12px 36px rgba(124, 58, 237, 0.2);
  z-index: 100;
  overflow: hidden;
}

.dark .search-dropdown {
  background: rgba(24, 19, 48, 0.95);
  border-color: rgba(192, 132, 252, 0.3);
  box-shadow: 0 12px 36px rgba(0, 0, 0, 0.5);
}

.dropdown-header {
  padding: 10px 16px;
  font-size: 0.75rem;
  font-weight: 600;
  color: #7C3AED;
  background: rgba(124, 58, 237, 0.05);
  border-bottom: 1px solid rgba(124, 58, 237, 0.08);
}

.dark .dropdown-header {
  color: #C084FC;
  background: rgba(192, 132, 252, 0.08);
}

.dropdown-empty {
  padding: 16px;
  font-size: 0.85rem;
  color: #71698A;
  text-align: center;
}

.dropdown-list {
  max-height: 340px;
  overflow-y: auto;
  padding: 6px;
}

.dropdown-item {
  display: block;
  padding: 10px 12px;
  border-radius: 10px;
  text-decoration: none !important;
  transition: background 0.2s ease;
}

.dropdown-item:hover {
  background: rgba(124, 58, 237, 0.08);
}

.dark .dropdown-item:hover {
  background: rgba(192, 132, 252, 0.12);
}

.item-title-row {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 4px;
}

.item-category-tag {
  font-size: 0.7rem;
  font-weight: 600;
  padding: 2px 8px;
  border-radius: 999px;
  background: rgba(124, 58, 237, 0.1);
  color: #7C3AED;
}

.dark .item-category-tag {
  background: rgba(192, 132, 252, 0.15);
  color: #C084FC;
}

.item-title {
  font-size: 0.9rem;
  font-weight: 600;
  color: #1F1B2E;
}

.dark .item-title {
  color: #FFF;
}

.item-path {
  font-size: 0.75rem;
  color: #948CAE;
}

.nav-center {
  display: flex;
  align-items: center;
  gap: 28px;
  margin-left: auto;
}

.nav-item {
  font-size: 0.95rem;
  font-weight: 500;
  color: #645D78;
  text-decoration: none;
  position: relative;
  padding: 4px 0;
  transition: color 0.2s ease;
}

.dark .nav-item {
  color: #A5A0BA;
}

.nav-item:hover, .nav-item.active {
  color: #7C3AED;
  font-weight: 600;
}

.dark .nav-item:hover, .dark .nav-item.active {
  color: #C084FC;
}

.nav-item.active::after {
  content: '';
  position: absolute;
  bottom: -4px;
  left: 50%;
  transform: translateX(-50%);
  width: 20px;
  height: 3px;
  border-radius: 3px;
  background: #7C3AED;
}

.dark .nav-item.active::after {
  background: #C084FC;
}

.nav-right {
  display: flex;
  align-items: center;
  gap: 16px;
  margin-left: 20px;
}

.theme-switch-btn {
  width: 44px;
  height: 24px;
  border-radius: 999px;
  background: rgba(124, 58, 237, 0.1);
  border: 1px solid rgba(124, 58, 237, 0.18);
  position: relative;
  cursor: pointer;
  padding: 0;
  display: flex;
  align-items: center;
  transition: all 0.3s ease;
}

.dark .theme-switch-btn {
  background: rgba(192, 132, 252, 0.15);
  border-color: rgba(192, 132, 252, 0.3);
}

.switch-thumb {
  width: 18px;
  height: 18px;
  border-radius: 50%;
  background: #FFFFFF;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.15);
  position: absolute;
  left: 3px;
  transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1), background 0.3s ease;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #7C3AED;
}

.theme-switch-btn.is-dark .switch-thumb {
  transform: translateX(20px);
  background: #181330;
  color: #C084FC;
}

.nav-divider {
  color: #D1CBE3;
  font-size: 14px;
}

.github-icon-link {
  color: #4A435E;
  display: flex;
  align-items: center;
  transition: color 0.2s ease;
}

.dark .github-icon-link {
  color: #D1CBE3;
}

.github-icon-link:hover {
  color: #7C3AED;
}

/* 2. Hero Section */
.hero-section {
  display: grid;
  grid-template-columns: 1.1fr 0.9fr;
  gap: 40px;
  align-items: center;
  padding: 30px 0 60px;
}

@media (max-width: 960px) {
  .hero-section {
    grid-template-columns: 1fr;
  }
}

.hero-title {
  font-size: 3.2rem;
  font-weight: 800;
  line-height: 1.25;
  letter-spacing: -0.02em;
  margin-bottom: 16px;
}

.gradient-text {
  background: linear-gradient(135deg, #7C3AED 0%, #C084FC 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.hero-subtitle {
  font-size: 1.25rem;
  font-weight: 600;
  color: #58506E;
  margin-bottom: 12px;
}

.dark .hero-subtitle {
  color: #B5AFC9;
}

.hero-desc {
  font-size: 1rem;
  line-height: 1.6;
  color: #766E8F;
  max-width: 520px;
  margin-bottom: 32px;
}

.dark .hero-desc {
  color: #9C95B3;
}

.hero-actions {
  display: flex;
  align-items: center;
  gap: 16px;
  margin-bottom: 28px;
}

.btn-primary {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 12px 28px;
  border-radius: 999px;
  background: linear-gradient(135deg, #7C3AED 0%, #6366F1 100%);
  color: #FFF;
  font-weight: 600;
  font-size: 0.95rem;
  text-decoration: none;
  box-shadow: 0 8px 24px rgba(124, 58, 237, 0.3);
  transition: all 0.25s ease;
}

.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 12px 30px rgba(124, 58, 237, 0.45);
}

.btn-secondary {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 12px 24px;
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.9);
  border: 1px solid #D8B4FE;
  color: #38304D;
  font-weight: 600;
  font-size: 0.95rem;
  text-decoration: none;
  transition: all 0.25s ease;
}

.dark .btn-secondary {
  background: rgba(255, 255, 255, 0.05);
  border-color: rgba(192, 132, 252, 0.3);
  color: #ECE8FA;
}

.btn-secondary:hover {
  border-color: #7C3AED;
  color: #7C3AED;
  background: #FFF;
}

.hero-badges {
  display: flex;
  gap: 12px;
}

.badge-pill {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 6px 16px;
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.7);
  border: 1px solid rgba(124, 58, 237, 0.15);
  font-size: 0.85rem;
  font-weight: 500;
  color: #554D6B;
}

.dark .badge-pill {
  background: rgba(255, 255, 255, 0.04);
  color: #C5BFDA;
  border-color: rgba(139, 92, 246, 0.2);
}

/* 3D Stage & Code Box Right */
.hero-right {
  position: relative;
  display: flex;
  justify-content: center;
}

.stage-container {
  position: relative;
  width: 100%;
  max-width: 480px;
  height: 380px;
}

/* Code Window */
.code-window {
  position: absolute;
  top: 10px;
  left: 20px;
  width: 360px;
  background: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(20px);
  border: 1px solid rgba(255, 255, 255, 0.8);
  border-radius: 16px;
  box-shadow: 0 20px 40px rgba(124, 58, 237, 0.15);
  overflow: hidden;
  z-index: 3;
}

.dark .code-window {
  background: rgba(24, 19, 48, 0.9);
  border-color: rgba(139, 92, 246, 0.3);
}

.window-header {
  padding: 10px 14px;
  background: rgba(124, 58, 237, 0.05);
  border-bottom: 1px solid rgba(124, 58, 237, 0.08);
}

.window-dots {
  display: flex;
  gap: 6px;
}

.dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
}
.dot.red { background: #FF5F56; }
.dot.yellow { background: #FFBD2E; }
.dot.green { background: #27C93F; }

.code-content {
  padding: 16px;
  font-family: "Fira Code", Consolas, Monaco, monospace;
  font-size: 0.85rem;
  line-height: 1.5;
  color: #38324C;
}

.dark .code-content {
  color: #E2DCF8;
}

.code-comment { color: #10B981; }
.kwd { color: #7C3AED; font-weight: 600; }
.var { color: #2563EB; }
.key { color: #D97706; }
.str { color: #EC4899; }
.indent { padding-left: 18px; }

/* Floating Cards */
.floating-card {
  position: absolute;
  background: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(12px);
  border: 1px solid rgba(255, 255, 255, 0.8);
  border-radius: 12px;
  box-shadow: 0 10px 25px rgba(124, 58, 237, 0.12);
  z-index: 4;
}

.dark .floating-card {
  background: rgba(28, 22, 54, 0.9);
  border-color: rgba(139, 92, 246, 0.25);
}

.float-code-icon {
  top: 40px;
  left: -20px;
  padding: 12px 16px;
  color: #7C3AED;
  font-weight: 800;
  font-size: 1.2rem;
}

.float-editor {
  top: 60px;
  right: -10px;
  padding: 12px;
  display: flex;
  align-items: center;
  gap: 8px;
}

.lines-placeholder .line {
  height: 4px;
  border-radius: 2px;
  background: #CBD5E1;
  margin-bottom: 4px;
}
.line-short { width: 30px; }
.line-long { width: 50px; background: #8B5CF6 !important; }

.float-chart {
  bottom: 90px;
  right: -15px;
  padding: 10px;
  width: 90px;
}

/* 3D Pedestal Stage */
.pedestal-stage {
  position: absolute;
  bottom: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 320px;
  height: 180px;
  z-index: 1;
}

.pedestal-disc {
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
  border-radius: 50%;
}

.disc-1 {
  bottom: 0;
  width: 320px;
  height: 80px;
  background: linear-gradient(180deg, #E6DEF8 0%, #D8CDF5 100%);
  box-shadow: 0 15px 35px rgba(124, 58, 237, 0.2);
}

.dark .disc-1 {
  background: linear-gradient(180deg, #2A214A 0%, #1E1738 100%);
}

.disc-2 {
  bottom: 25px;
  width: 240px;
  height: 60px;
  background: linear-gradient(180deg, #F3EEFE 0%, #E4DAF9 100%);
  border: 2px solid #C084FC;
  box-shadow: 0 0 20px rgba(192, 132, 252, 0.5);
}

.dark .disc-2 {
  background: linear-gradient(180deg, #3A2E63 0%, #291F4A 100%);
}

.disc-3 {
  bottom: 45px;
  width: 170px;
  height: 40px;
  background: #FFF;
}

.dark .disc-3 {
  background: #4C3C82;
}

.crystal-cube {
  position: absolute;
  bottom: 60px;
  left: 30px;
  width: 48px;
  height: 48px;
  background: linear-gradient(135deg, #A855F7, #6366F1);
  transform: rotate(45deg);
  border-radius: 8px;
  box-shadow: 0 0 25px rgba(168, 85, 247, 0.8);
  z-index: 2;
}

/* 3. 5 Feature Cards Row */
.feature-cards-row {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 16px;
  margin-bottom: 50px;
}

@media (max-width: 1024px) {
  .feature-cards-row {
    grid-template-columns: repeat(3, 1fr);
  }
}

@media (max-width: 640px) {
  .feature-cards-row {
    grid-template-columns: 1fr;
  }
}

.feature-card {
  background: rgba(255, 255, 255, 0.85);
  backdrop-filter: blur(12px);
  border: 1px solid rgba(255, 255, 255, 0.8);
  border-radius: 20px;
  padding: 20px;
  text-decoration: none !important;
  color: inherit;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  transition: all 0.25s ease;
  box-shadow: 0 4px 16px rgba(124, 58, 237, 0.04);
  position: relative;
}

.dark .feature-card {
  background: rgba(24, 19, 48, 0.7);
  border-color: rgba(139, 92, 246, 0.15);
}

.feature-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 30px rgba(124, 58, 237, 0.15);
  border-color: #C084FC;
}

.card-icon-box {
  width: 44px;
  height: 44px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 14px;
}

.bg-purple-1 { background: linear-gradient(135deg, #7C3AED, #9333EA); }
.bg-purple-2 { background: linear-gradient(135deg, #8B5CF6, #A855F7); }
.bg-pink-1 { background: linear-gradient(135deg, #C084FC, #E879F9); }
.bg-indigo-1 { background: linear-gradient(135deg, #6366F1, #818CF8); }
.bg-violet-1 { background: linear-gradient(135deg, #7C3AED, #A855F7); }

.card-title {
  font-size: 1.05rem;
  font-weight: 700;
  margin-bottom: 8px;
  color: #1F1B2E;
}

.dark .card-title {
  color: #FFF;
}

.card-desc {
  font-size: 0.85rem;
  line-height: 1.5;
  color: #71698A;
}

.dark .card-desc {
  color: #A39CBD;
}

.card-arrow {
  align-self: flex-end;
  font-size: 12px;
  color: #A855F7;
  margin-top: 12px;
}

/* 4. Bottom Grid Section */
.bottom-section-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 24px;
}

@media (max-width: 860px) {
  .bottom-section-grid {
    grid-template-columns: 1fr;
  }
}

.column-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 16px;
}

.header-left {
  display: flex;
  align-items: center;
  gap: 8px;
}

.header-icon {
  font-size: 1.2rem;
}

.column-title {
  font-size: 1.25rem;
  font-weight: 700;
  color: #1F1B2E;
}

.dark .column-title {
  color: #FFF;
}

.more-link {
  font-size: 0.85rem;
  font-weight: 600;
  color: #7C3AED;
  text-decoration: none;
}

.notes-list {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.note-item-card {
  display: flex;
  gap: 16px;
  background: rgba(255, 255, 255, 0.85);
  backdrop-filter: blur(12px);
  border: 1px solid rgba(255, 255, 255, 0.8);
  border-radius: 16px;
  padding: 16px;
  text-decoration: none !important;
  color: inherit;
  transition: all 0.25s ease;
}

.dark .note-item-card {
  background: rgba(24, 19, 48, 0.7);
  border-color: rgba(139, 92, 246, 0.15);
}

.note-item-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 20px rgba(124, 58, 237, 0.12);
  border-color: #C084FC;
}

.note-thumb {
  width: 100px;
  height: 70px;
  border-radius: 10px;
  background: linear-gradient(135deg, #8B5CF6 0%, #6366F1 100%);
  flex-shrink: 0;
  position: relative;
  overflow: hidden;
}

.thumb-2 {
  background: linear-gradient(135deg, #7C3AED 0%, #C084FC 100%);
}

.note-content {
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.note-title {
  font-size: 1rem;
  font-weight: 700;
  margin-bottom: 6px;
  color: #1F1B2E;
}

.dark .note-title {
  color: #FFF;
}

.note-summary {
  font-size: 0.825rem;
  color: #71698A;
  margin-bottom: 8px;
  line-height: 1.4;
}

.dark .note-summary {
  color: #A39CBD;
}

.note-meta {
  font-size: 0.75rem;
  color: #948CAE;
  display: flex;
  gap: 6px;
}

/* Projects Column */
.project-item-card {
  background: rgba(255, 255, 255, 0.85);
  backdrop-filter: blur(12px);
  border: 1px solid rgba(255, 255, 255, 0.8);
  border-radius: 16px;
  padding: 24px;
}

.dark .project-item-card {
  background: rgba(24, 19, 48, 0.7);
  border-color: rgba(139, 92, 246, 0.15);
}

.project-header {
  display: flex;
  gap: 16px;
  margin-bottom: 16px;
}

.project-logo {
  width: 48px;
  height: 48px;
  border-radius: 14px;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #FFF;
  box-shadow: 0 6px 16px rgba(124, 58, 237, 0.25);
}

.project-logo-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.project-name {
  font-size: 1.15rem;
  font-weight: 700;
  color: #1F1B2E;
  margin-bottom: 4px;
}

.dark .project-name {
  color: #FFF;
}

.project-desc {
  font-size: 0.875rem;
  color: #71698A;
}

.dark .project-desc {
  color: #A39CBD;
}

.project-tags {
  display: flex;
  gap: 8px;
  margin-bottom: 16px;
}

.ptag {
  padding: 4px 12px;
  border-radius: 999px;
  background: rgba(124, 58, 237, 0.08);
  color: #7C3AED;
  font-size: 0.75rem;
  font-weight: 600;
}

.dark .ptag {
  background: rgba(192, 132, 252, 0.12);
  color: #C084FC;
}

.project-stats {
  display: flex;
  gap: 16px;
  font-size: 0.85rem;
  color: #71698A;
}
</style>
