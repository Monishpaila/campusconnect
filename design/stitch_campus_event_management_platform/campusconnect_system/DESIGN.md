---
name: CampusConnect System
colors:
  surface: '#f9f9ff'
  surface-dim: '#cfdaf2'
  surface-bright: '#f9f9ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f0f3ff'
  surface-container: '#e7eeff'
  surface-container-high: '#dee8ff'
  surface-container-highest: '#d8e3fb'
  on-surface: '#111c2d'
  on-surface-variant: '#464554'
  inverse-surface: '#263143'
  inverse-on-surface: '#ecf1ff'
  outline: '#767586'
  outline-variant: '#c7c4d7'
  surface-tint: '#494bd6'
  primary: '#4648d4'
  on-primary: '#ffffff'
  primary-container: '#6063ee'
  on-primary-container: '#fffbff'
  inverse-primary: '#c0c1ff'
  secondary: '#0051d5'
  on-secondary: '#ffffff'
  secondary-container: '#316bf3'
  on-secondary-container: '#fefcff'
  tertiary: '#712ae2'
  on-tertiary: '#ffffff'
  tertiary-container: '#8a4cfc'
  on-tertiary-container: '#fffbff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e1e0ff'
  primary-fixed-dim: '#c0c1ff'
  on-primary-fixed: '#07006c'
  on-primary-fixed-variant: '#2f2ebe'
  secondary-fixed: '#dbe1ff'
  secondary-fixed-dim: '#b4c5ff'
  on-secondary-fixed: '#00174b'
  on-secondary-fixed-variant: '#003ea8'
  tertiary-fixed: '#eaddff'
  tertiary-fixed-dim: '#d2bbff'
  on-tertiary-fixed: '#25005a'
  on-tertiary-fixed-variant: '#5a00c6'
  background: '#f9f9ff'
  on-background: '#111c2d'
  surface-variant: '#d8e3fb'
typography:
  display:
    fontFamily: Plus Jakarta Sans
    fontSize: 3rem
    fontWeight: '800'
    lineHeight: 3.5rem
    letterSpacing: -0.025em
  headline-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 2.25rem
    fontWeight: '700'
    lineHeight: 2.75rem
    letterSpacing: -0.02em
  headline-lg-mobile:
    fontFamily: Plus Jakarta Sans
    fontSize: 1.75rem
    fontWeight: '700'
    lineHeight: 2.25rem
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 1.5rem
    fontWeight: '600'
    lineHeight: 2rem
    letterSpacing: -0.015em
  headline-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 1.25rem
    fontWeight: '600'
    lineHeight: 1.75rem
    letterSpacing: -0.01em
  title:
    fontFamily: Inter
    fontSize: 1.125rem
    fontWeight: '600'
    lineHeight: 1.625rem
  body-lg:
    fontFamily: Inter
    fontSize: 1rem
    fontWeight: '400'
    lineHeight: 1.5rem
  body-md:
    fontFamily: Inter
    fontSize: 0.875rem
    fontWeight: '400'
    lineHeight: 1.375rem
  body-sm:
    fontFamily: Inter
    fontSize: 0.75rem
    fontWeight: '400'
    lineHeight: 1.125rem
  label-md:
    fontFamily: Inter
    fontSize: 0.875rem
    fontWeight: '500'
    lineHeight: 1.25rem
    letterSpacing: 0.01em
  label-sm:
    fontFamily: Inter
    fontSize: 0.75rem
    fontWeight: '600'
    lineHeight: 1rem
    letterSpacing: 0.02em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  gutter: 1.5rem
  gutter-mobile: 1rem
  margin: 2rem
  margin-mobile: 1rem
  space-xs: 0.25rem
  space-sm: 0.5rem
  space-md: 1rem
  space-lg: 1.5rem
  space-xl: 2rem
---

## Brand & Style

The design system establishes an energetic, reliable, and modern SaaS aesthetic tailored for collegiate life and academic event operations. It balances the clarity of institutional software with the dynamic momentum of student social life and co-curricular programming. 

The aesthetic is clean, light, and airy—prioritizing immediate legibility, high task throughput, and effortless scanning. Tactile micro-interactions, subtle layered shadows, and crisp neutral boundaries create a spatial environment where dense event schedules, registration workflows, and administrative dashboards feel organized rather than overwhelming.

Key brand tenets include:
- **Clarity & Light:** High-key backgrounds dominated by pristine whites and cool off-white slates, avoiding heavy or gloomy surfaces.
- **Academic Vitality:** Vibrant indigo-violet paired with electric royal blue to convey forward-thinking scholarship, energy, and community.
- **Modular Efficiency:** Composable UI containers engineered to shift effortlessly between student-facing discovery views and high-density administrative operations.

## Colors

The palette is rooted in an energetic dual-accent strategy of vibrant indigo-violet (`#6366F1`) and royal blue (`#2563EB`), supported by rich deep violet accents (`#7C3AED`) and anchored by foundational slate neutrals (`#1E293B`, `#64748B`, `#E2E8F0`).

### Semantic Color Assignments
- **Canvas / Background:** `#FFFFFF` as the primary base canvas; `#F8FAFC` (Slate-50) for outer app shells, background rails, and subtle structural alternates.
- **Surfaces & Cards:** Pure `#FFFFFF` elevated above slate backdrops to ensure clear component boundaries.
- **Borders & Dividers:** Subtle `#E2E8F0` (Slate-200) for structural lines, table borders, and input strokes.
- **Typography:** `#0F172A` (Slate-900) for primary headings; `#1E293B` (Slate-800) for default body; `#64748B` (Slate-500) for secondary metadata and timestamps; `#94A3B8` (Slate-400) for disabled states and placeholders.
- **Interactive Accents:** 
  - Primary button & action fills: `#6366F1` transitioning to `#4F46E5` on hover.
  - Active navigation indicators & selected pills: `#2563EB` with subtle 10% tint backgrounds (`#EFF6FF`).
  - Elevated status items & role highlights: Deep violet `#7C3AED`.

### Event Status Tokens
- **Upcoming:** Lavender tint (`#EEF2FF`) background, `#4F46E5` label, `#C7D2FE` subtle border.
- **Active / Happening Now:** Emerald tint (`#ECFDF5`) background, `#059669` label, glowing pulse indicator `#10B981`.
- **Full / Waitlist:** Amber tint (`#FFFBEB`) background, `#D97706` label, `#FDE68A` border.
- **Completed:** Neutral slate tint (`#F1F5F9`) background, `#64748B` label, `#E2E8F0` border.

## Typography

The typographic hierarchy utilizes **Plus Jakarta Sans** for display, section titles, and event titles, imbuing the brand with a friendly, high-energy, contemporary personality. For functional utility, data tables, microcopy, form controls, and multi-line descriptive text, **Inter** provides unmatched legibility and neutral systematic rendering across varying screen densities.

### Hierarchy & Usage
- **Display & Major Section Titles (`display`, `headline-lg`):** Reserved for hero registration headers, campus milestone cards, and portal landing areas. Tightly tracked (`-0.025em`) for modern punch.
- **Card & Component Headlines (`headline-md`, `headline-sm`):** Applied to individual event card headers, modal dialog titles, and metric widget values.
- **Standard Content (`body-md`, `body-lg`):** Standard reading level for event agendas, speaker biographies, and transactional instructions.
- **Data & Micro-copy (`label-sm`, `label-md`, `body-sm`):** Applied to role switcher tabs, badge markers, table header keys, and form field helper annotations.

## Layout & Spacing

The layout model employs a fluid 12-column grid system resting inside a maximum content width of `1280px` (`max-w-7xl`), flanked by safe outer canvas margins.

### Breakpoint Structure
- **Desktop (≥ 1024px):** 12 columns, `1.5rem` (`24px`) gutters, `2rem` (`32px`) margins. Sidebars for navigation and category filters remain permanently expanded or docked.
- **Tablet (768px – 1023px):** 8 columns, `1.5rem` gutters, `1.5rem` margins. Sidebars collapse to responsive top action bars or overlay drawers; grid transforms into 2-column card layouts.
- **Mobile (< 768px):** 4 columns, `1rem` (`16px`) gutters, `1rem` (`16px`) outer canvas margins. All multi-column cards collapse to single-column feeds, while metrics and role controls adopt horizontally scrollable or compact segment patterns.

### Component Spacing Rhythm
- **Internal Card Padding:** `1.5rem` for high-level summaries and modal shells; `1.25rem` for standard discovery cards; `0.75rem` to `1rem` for nested sub-cards.
- **Form Groups & Field Stack:** `1rem` vertical separation between inputs; `0.375rem` between label and input box.
- **Inline Icon Gaps:** Consistent `0.5rem` (`space-sm`) margin between Lucide icons and accompanying text strings.

## Elevation & Depth

Visual hierarchy relies on soft, multi-layered shadows coupled with crisp, low-contrast slate boundaries (`#E2E8F0`). Dark, harsh drop shadows are strictly avoided to sustain the clean light-mode atmosphere.

### Depth Tiers
1. **Level 0 (Flat Canvas):** `#F8FAFC` (Slate-50) background surfaces, nested table rows, and secondary filter rails. Borderless or anchored purely by `1px` lines.
2. **Level 1 (Card & Content Blocks):** Pure white surfaces bordered with `1px solid #E2E8F0` and elevated with an ambient glow:
   - `box-shadow: 0 1px 3px 0 rgba(15, 23, 42, 0.05), 0 1px 2px -1px rgba(15, 23, 42, 0.05);`
3. **Level 2 (Interactive Hover & Dropdowns):** Used on event cards upon cursor focus, popover menus, and date pickers:
   - `box-shadow: 0 10px 15px -3px rgba(15, 23, 42, 0.06), 0 4px 6px -4px rgba(15, 23, 42, 0.04);`
   - Active cards lift with a `-2px` transform on the Y-axis.
4. **Level 3 (Modal Dialogs & Slide-overs):** Center-screen confirmation overlays and ticket preview sheets:
   - `box-shadow: 0 20px 25px -5px rgba(15, 23, 42, 0.08), 0 8px 10px -6px rgba(15, 23, 42, 0.04);`
   - Supported by a blurred neutral overlay: `backdrop-filter: blur(4px); background-color: rgba(15, 23, 42, 0.4);`

## Shapes

The design system embraces a friendly, rounded aesthetic that strikes a balance between sleek enterprise software and youthful student engagement. 

### Corner Radius System
- **Base Components (`rounded-md` / `0.5rem`):** Text inputs, dropdown select triggers, calendar day selectors, and table containers.
- **Cards & Summary Modules (`rounded-xl` / `1rem`):** Standard event cards, stats widgets, and secondary dashboard blocks.
- **Modals & Hero Banners (`rounded-2xl` / `1.5rem`):** Modal dialog windows, large promotional highlight carousels, and registration preview panels.
- **Pills & Status Controls (`rounded-full` / `9999px`):** Status badges, role switcher toggles, user avatars, tag chips, and icon action circles.

## Components

### 1. Role Switcher
- **Structure:** Positioned persistently in the upper-right application header. Rendered as a pill container (`rounded-full`) with a subtle `#F1F5F9` background and `1px solid #E2E8F0`.
- **Options:** Segmented tabs for "Student", "Organizer", and "Admin".
- **Selected State:** Active segment transitions with an animated sliding white capsule (`#FFFFFF`) backed by `shadow-sm`, with text styled in `#1E293B` font-semibold.
- **Micro-indicator:** Admin option shows a miniature crown or shield Lucide icon (`w-3.5 h-3.5`) in `#7C3AED`.

### 2. Buttons
- **Primary:** Solid `#6366F1` background, `#FFFFFF` text, `rounded-xl`, `h-10 px-4` (medium) or `h-12 px-6` (large). Transitions to `#4F46E5` on hover. 
- **Secondary:** Subtle royal blue tint (`#EFF6FF`), `#2563EB` text, `1px solid #DBEAFE`. Hover states shift to `#DBEAFE`.
- **Outline:** Pure `#FFFFFF` background, `#1E293B` text, `1px solid #E2E8F0`. Hover triggers `#F8FAFC` background and `#0F172A` text.
- **Icon Attachment:** Lucide icons sized to `18px` with `0.5rem` margin preceding or following the label.

### 3. Event Badges & Status Indicators
- **Form:** Compact, full-pill (`rounded-full`) inline elements styled with `py-0.5 px-2.5` and `font-semibold text-xs`.
- **Variants:**
  - *Upcoming:* Tinted Indigo (`bg-indigo-50 text-indigo-700 border border-indigo-200`).
  - *Active:* Light Emerald (`bg-emerald-50 text-emerald-700 border border-emerald-200`) with an inline pulsing `w-1.5 h-1.5` dot.
  - *Full / Waitlist:* Warm Amber (`bg-amber-50 text-amber-800 border border-amber-200`).
  - *Completed:* Soft Slate (`bg-slate-100 text-slate-600 border border-slate-200`).

### 4. Stats Summary Cards
- **Styling:** White surface (`#FFFFFF`), `rounded-xl`, `p-5`, bordered with `#E2E8F0`, ambient `shadow-sm`.
- **Content Structure:** 
  - Top row: Metric label in `label-sm` (`#64748B`) paired with a `rounded-lg` Lucide icon container (e.g., `#EEF2FF` fill with `#6366F1` icon).
  - Middle: Metric count rendered in `headline-md` (`#0F172A`).
  - Bottom: Delta badge (`+12% vs last month`) or capacity progress bar.

### 5. Input Fields & Search Bars
- **Containers:** Height of `42px`, `rounded-lg`, `border: 1px solid #CBD5E1`, background `#FFFFFF`, text `#0F172A`.
- **States:** Focus produces `border-color: #6366F1` and a `ring-2 ring-indigo-500/20` box shadow.
- **Add-ons:** Left-aligned Lucide `Search` icon in `#94A3B8`; right-aligned clear buttons or filter tags.

### 6. Tabular Data Views
- **Header:** Sticky `#F8FAFC` row, uppercase `text-xs font-semibold` in `#64748B`, with explicit vertical divider alignment.
- **Row Styling:** Hover states trigger `#F8FAFC` smooth transitions. Bottom borders styled with `1px solid #F1F5F9`.
- **Controls:** Inline action buttons (e.g., "Manage", "Check-in", "Export") styled as compact ghost buttons (`h-8 px-2 text-xs`).

### 7. Modal Dialogs
- **Window:** Centered `max-w-lg` to `max-w-2xl`, background `#FFFFFF`, `rounded-2xl`, `p-6` to `p-8`, with sharp close triggers in the top-right.
- **Backdrop:** `#0F172A` with `40%` opacity and `4px` blur.
- **Footer:** Right-aligned actions, secondary cancel button adjacent to primary confirmation button.

### 8. Lucide Icon Conventions
- **Stroke Width:** Universally set to `1.75px` for a crisp, balanced optical weight alongside Inter text.
- **Standard Sizing:** `16px` (`w-4 h-4`) inside badges and dense tables; `20px` (`w-5 h-5`) within standard form inputs and action buttons; `24px` (`w-6 h-6`) within metric highlight tiles.