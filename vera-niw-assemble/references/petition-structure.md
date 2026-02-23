# NIW Petition .docx Formatting Specification

*Read this before generating any docx-js code in NIW_Assemble.*

This file defines the exact docx-js setup, styles, and section templates
for attorney-quality NIW petition letters. Follow exactly — inconsistent
formatting across pages signals an unprofessional submission.

---

## Page Setup

```javascript
// US Letter, 1-inch margins, no headers/footers except page numbers
sections: [{
  properties: {
    page: {
      size: { width: 12240, height: 15840 },  // US Letter in DXA
      margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 }  // 1 inch
    }
  },
  footers: {
    default: new Footer({
      children: [new Paragraph({
        alignment: AlignmentType.CENTER,
        children: [new TextRun({ children: [PageNumber.CURRENT] })]
      })]
    })
  },
  children: [/* all content */]
}]
```

---

## Document Styles

```javascript
const doc = new Document({
  styles: {
    default: {
      document: { run: { font: "Arial", size: 24 } }  // 12pt body
    },
    paragraphStyles: [
      {
        id: "Heading1", name: "Heading 1",
        basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 28, bold: true, font: "Arial", color: "000000" },
        paragraph: {
          spacing: { before: 360, after: 180 },
          outlineLevel: 0
        }
      },
      {
        id: "Heading2", name: "Heading 2",
        basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 24, bold: true, font: "Arial", color: "000000" },
        paragraph: {
          spacing: { before: 240, after: 120 },
          outlineLevel: 1
        }
      },
      {
        id: "Heading3", name: "Heading 3",
        basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 24, bold: false, underline: {}, font: "Arial" },
        paragraph: {
          spacing: { before: 180, after: 60 },
          outlineLevel: 2
        }
      }
    ]
  }
});
```

---

## Paragraph Spacing

```javascript
// Standard body paragraph
new Paragraph({
  children: [new TextRun("Body text here.")],
  spacing: { after: 160 }  // ~8pt after each paragraph
})

// Paragraph with no extra space (e.g., inside lists)
new Paragraph({
  children: [new TextRun("List item.")],
  spacing: { after: 80 }
})
```

---

## Section Headings Pattern

Each of the 9 petition sections uses Heading 1.
Each prong within a section uses Heading 2.
Sub-sections (e.g., 3.1, 3.2) use Heading 3.

```javascript
// Section heading (e.g., "I. PROPOSED ENDEAVOR")
new Paragraph({
  heading: HeadingLevel.HEADING_1,
  children: [new TextRun("I. PROPOSED ENDEAVOR")]
})

// Prong heading (e.g., "Prong 1A: Distinguished from Routine Practice")
new Paragraph({
  heading: HeadingLevel.HEADING_2,
  children: [new TextRun("Prong 1A: Distinguished from Routine Practice")]
})

// Sub-section heading (e.g., "1.1 Nationwide Critical Problem")
new Paragraph({
  heading: HeadingLevel.HEADING_3,
  children: [new TextRun("1.1 Nationwide Critical Problem")]
})
```

---

## Section Numbering Convention

Use Roman numerals for section titles in the heading:

```
I.    INTRODUCTION
II.   PROPOSED ENDEAVOR
III.  ACADEMIC CREDENTIALS AND RECOGNITION
IV.   PILLAR 1: [TITLE]
V.    PILLAR 2: [TITLE]
VI.   PILLAR 3: [TITLE]
VII.  THE NATIONAL INTEREST SUBSTANTIALLY OUTWEIGHS THE LABOR CERTIFICATION REQUIREMENT
VIII. CONCLUSION
IX.   EXHIBIT INDEX
```

---

## Publications Table (Section III)

```javascript
// Column widths for US Letter, 1" margins (content = 9360 DXA total)
// Title: 4000 | Venue: 2500 | Year: 600 | Citations: 800 | Role: 1460
const border = { style: BorderStyle.SINGLE, size: 1, color: "CCCCCC" };
const cellBorders = { top: border, bottom: border, left: border, right: border };
const cellMargins = { top: 80, bottom: 80, left: 120, right: 120 };

// Header row
new TableRow({
  tableHeader: true,
  children: [
    headerCell("#", 400),
    headerCell("Title", 4000),
    headerCell("Venue", 2360),
    headerCell("Year", 600),
    headerCell("Cit.", 800),
    headerCell("Role", 1200),
  ]
})

// Helper for header cell
function headerCell(text, width) {
  return new TableCell({
    borders: cellBorders,
    width: { size: width, type: WidthType.DXA },
    margins: cellMargins,
    shading: { fill: "E8F0F8", type: ShadingType.CLEAR },
    children: [new Paragraph({
      children: [new TextRun({ text, bold: true, size: 20 })]
    })]
  });
}

// Data row
function dataCell(text, width, bold = false) {
  return new TableCell({
    borders: cellBorders,
    width: { size: width, type: WidthType.DXA },
    margins: cellMargins,
    children: [new Paragraph({
      children: [new TextRun({ text: String(text), bold, size: 20 })]
    })]
  });
}
```

Column widths: `400 + 4000 + 2360 + 600 + 800 + 1200 = 9360` ✓

---

## Exhibit Index Table (Section IX)

```javascript
// Two columns: Exhibit # and Description
// 1200 | 8160 = 9360 total
new Table({
  width: { size: 9360, type: WidthType.DXA },
  columnWidths: [1200, 8160],
  rows: [
    headerRow,
    ...exhibits.map((ex, i) =>
      new TableRow({ children: [
        dataCell(`Exhibit ${i + 1}`, 1200, true),
        dataCell(ex.description, 8160),
      ]})
    )
  ]
})
```

---

## Prose to Paragraphs Conversion

Pillar prose comes as multi-paragraph text strings. Convert to Paragraph
elements by splitting on double newlines:

```javascript
function textToParagraphs(text) {
  return text
    .split(/\n\n+/)
    .filter(p => p.trim().length > 0)
    .map(p => new Paragraph({
      children: [new TextRun(p.trim())],
      spacing: { after: 160 }
    }));
}
```

For headings embedded in prose (lines starting with `####`, `###`, `##`):
Strip the markdown heading markers and convert to the appropriate
HeadingLevel before creating the Paragraph.

---

## Page Break Between Major Sections

```javascript
// Add before each new major section (Sections IV, V, VI, VII, VIII, IX)
new Paragraph({
  children: [new PageBreak()]
})
```

Do NOT add page breaks between prongs within the same pillar section.

---

## Critical Rules (from docx skill)

- Never use `\n` inside TextRun — use separate Paragraph elements
- Never use unicode bullets — use `LevelFormat.BULLET` with numbering config
- Always set table width with `WidthType.DXA` — never PERCENTAGE
- Tables need dual widths: `columnWidths` array AND `width` on each cell
- `columnWidths` must sum exactly to table total width
- Use `ShadingType.CLEAR` for table shading — never SOLID
- Page size must be set explicitly — docx-js defaults to A4

---

## Validation

After generating:
```bash
python /mnt/skills/public/docx/scripts/office/validate.py \
  /home/claude/niw_petition_[LastName].docx
```

If validation fails, unpack, inspect XML, fix, repack:
```bash
python /mnt/skills/public/docx/scripts/office/unpack.py \
  niw_petition_[LastName].docx unpacked/
# fix XML
python /mnt/skills/public/docx/scripts/office/pack.py \
  unpacked/ niw_petition_[LastName].docx
```
