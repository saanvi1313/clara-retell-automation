# Clara Retell Automation

This project builds a **zero-cost automation pipeline** that converts demo and onboarding call recordings into a deployable **Retell AI voice agent configuration**.

The system processes conversations, extracts structured operational rules, and generates versioned AI agent specifications.

The pipeline simulates the real onboarding workflow used by Clara Answers.

---

# Architecture

The automation consists of two pipelines.

## Pipeline A – Demo Call → Preliminary Agent (v1)

Demo Transcript
↓
Extract Account Memo
↓
Generate Retell Agent Spec
↓
Store versioned outputs (v1)

## Pipeline B – Onboarding Call → Updated Agent (v2)

Onboarding Transcript
↓
Extract Updates
↓
Update Account Memo
↓
Generate Updated Agent Spec
↓
Create Change Log

This separation ensures that **exploratory demo information is refined during onboarding**.

---

# Components

The system includes the following modules:

### Transcription

Audio recordings are transcribed locally using **OpenAI Whisper (open-source)**.

### Memo Extraction

Conversation data is converted into structured operational configuration including:

* business hours
* emergency routing
* services supported
* integration constraints
* after-hours behavior

### Agent Spec Generation

A **Retell agent configuration JSON** is generated containing:

* agent name
* system prompt
* call routing protocol
* fallback logic
* key variables

### Versioning

The system maintains configuration versions:

v1 → Generated from demo call
v2 → Updated from onboarding call

A changelog documents all modifications.

---

# Folder Structure

```
dataset/
   demo_calls/
   onboarding_calls/

scripts/
   transcribe_audio.py
   demo_pipeline.py
   onboarding_pipeline.py

outputs/
   accounts/<account_id>/
      v1/
      v2/
      changes.md

workflows/
   n8n_workflow.json
```

---

# Running the Pipeline

## 1 Install Dependencies

```
pip install -r requirements.txt
```

---

## 2 Transcribe Onboarding Audio

```
python scripts/transcribe_audio.py
```

This converts:

```
audio.m4a → audio.txt
```

---

## 3 Generate Initial Agent (Demo Pipeline)

```
python scripts/demo_pipeline.py
```

Outputs:

```
outputs/accounts/<account_id>/v1/
```

---

## 4 Apply Onboarding Updates

```
python scripts/onboarding_pipeline.py
```

Outputs:

```
outputs/accounts/<account_id>/v2/
```

---

# Output Artifacts

Each account generates:

```
memo.json
agent_spec.json
changes.md
```

Example structure:

```
outputs/accounts/bens_electric/

   v1/
      memo.json
      agent_spec.json

   v2/
      memo.json
      agent_spec.json

   changes.md
```

---

# Example Memo Fields

The structured memo includes:

* account_id
* company_name
* business_hours
* services_supported
* emergency_definition
* emergency_routing_rules
* non_emergency_routing_rules
* call_transfer_rules
* integration_constraints
* after_hours_flow_summary
* office_hours_flow_summary
* questions_or_unknowns

---

# Example Agent Spec Fields

Generated Retell configuration includes:

* agent_name
* voice_style
* system_prompt
* key_variables
* call_transfer_protocol
* fallback_protocol
* version

---

# n8n Workflow

A conceptual n8n workflow is provided in:

```
workflows/n8n_workflow.json
```

Pipeline stages:

File Input
↓
Transcription
↓
Memo Extraction
↓
Agent Spec Generation
↓
Store Outputs

---
## n8n Workflow

The automation workflow orchestrates the processing pipeline.

Manual Trigger
↓
Run Demo Pipeline (generate v1 memo + agent)
↓
Transcribe Onboarding Audio
↓
Run Onboarding Pipeline (update memo → v2 agent)
↓
Outputs stored in outputs/accounts/

# Zero-Cost Constraint

The pipeline runs entirely using free tools:

* Whisper (local transcription)
* Python scripts
* Local JSON storage

No paid APIs or subscriptions are required.

---

# Known Limitations

* Extraction logic is rule-based and may require refinement for more complex conversations.
* Retell API integration is simulated via agent spec JSON rather than direct deployment.
* The pipeline currently processes one account example but supports scaling to multiple accounts.

---

# Future Improvements

If production access were available:

* integrate with Retell API for automatic agent deployment
* add structured extraction using LLM models
* support batch processing for large onboarding datasets
* build a dashboard for account configuration management

---

# Summary

This project demonstrates how conversational data can be transformed into structured operational rules and deployed as AI answering agents through a reproducible automation pipeline.
