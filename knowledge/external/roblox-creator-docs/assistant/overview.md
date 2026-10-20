---
title: Assistant
description: Overview of Assistant, Roblox's AI helper.
tags: [roblox, documentation, external-reference, priority-reference, assistant]
hideInPageNavigation: true
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [assistant/overview.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/assistant/overview.md). Published page: [https://create.roblox.com/docs/assistant/overview](https://create.roblox.com/docs/assistant/overview).

export const sections = [
  {
    description: "Assistant is an AI helper that accelerates content creation by helping you get started, supplementing your skills, and assisting with ongoing development.",
    content: [
      {
        title: "Assistant for Studio",
        description: "In Roblox Studio, Assistant can act directly on the data model to write scripts, insert and modify objects, and automate repetitive tasks so that you can focus on creation.",
        image: "/assets/assistant/AssistantStudioExample.png",
        buttons: [
          { text: "Assistant for Studio guide", href: "assistant/guide"}
        ]
      },
      {
        title: "Assistant in the documentation",
        description: "Assistant is available directly from the documentation. Ask it to clarify concepts, provide sample code for a use case, or compare and contrast approaches to a problem.",
        image: "/assets/assistant/AssistantDocumentationSite.png"
      },
    ]
  }
];

{sections.map((section, index) => (
  <Grid xs={12} key={index}>
  <div style={{ marginTop: 16, marginBottom: 48 }}>
    {section.description && (
      <p>{section.description}</p>
    )}
  </div>
    {section.content.map((section, index) => (
      <Grid container spacing={8} key={index} style={{ marginTop: 24 }}>
        <Grid item xs={12} md={6}>
          <div>
            <h2>{section.title}</h2>
            <p>{section.description}</p>
            <div style={{ marginTop: 24, marginBottom: 48 }}>
              {section.buttons &&  section.buttons.map((button, btnIndex) => (
                <Button
                  key={btnIndex}
                  variant="contained"
                  color="secondary"
                  size="large"
                  href={button.href}
                >
                  {button.text}
                </Button>
              ))}
            </div>
          </div>
        </Grid>
        <Grid item xs={12} md={6}>
          <img
            src={section.image}
            alt={section.title}
          />
        </Grid>
      </Grid>
    ))}
  </Grid>
))}


## Related Files

- [[external/roblox-creator-docs/assistant/guide]] - Assistant for Studio.
- [[external/roblox-creator-docs/assistant/prompt-engineering]] - Assistant prompt guide and examples.
- [[external/roblox-creator-docs/assistant/mcp]] - MCP servers.
- [[external/roblox-creator-docs/assistant/skills]] - Skills.
