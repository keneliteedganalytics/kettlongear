# Supplier Outreach Ledger: Wholesale Lane

Sent 30 September 2026 by Kenneth Young (Elite-Edge-Analytics, LLC d/b/a Kettlon Gear). All bodies are in ops/SUPPLIER_OUTREACH_DRAFTS.md.

| # | Supplier | Product (ASIN) | Channel | Reply address to watch | Sent | Follow-up 1 due | Follow-up 2 due | Status |
|---|----------|----------------|---------|------------------------|------|-----------------|-----------------|--------|
| 1 | Modern Toyota Wholesale Parts (High Point, NC) | Toyota OEM oil filter 90915-YZZD3 (B0D6ZY8Z2L) | Web form, lead 14637 | any @moderntoyota.com; Parts desk 336-788-3003 | 30 Sep 2026 | 5 Oct 2026 | 12 Oct 2026 | Awaiting reply (checked 4 Oct 2026, no reply) |
| 2 | CarPro-US / Sky's the Limit Car Care | CarPro Eraser (B00NIEAN2A) | Email to Service@carpro-us.com; site account created | Service@carpro-us.com, any @carpro-us.com | 30 Sep 2026 | none | none | Declined 30 Sep 2026: no new Amazon resellers, brick-and-mortar detail shops only. Thanked. SKU needs a replacement. |
| 3 | Wahl Professional Animal | Pocket Pro Equine Trimmer (B00MNMDO3S) | Distributor web form (Amazon resale disclosed: Yes) | any @wahl.com, @wahlusa.com, @wahlpro.com | 30 Sep 2026 | 5 Oct 2026 | 12 Oct 2026 | Awaiting reply (checked 4 Oct 2026, no reply) |
| 4 | Reptile Supply Co. | Repashy Superfoods (B0D7JYJ99S) | Email to info@reptilesupplyco.com | info@reptilesupplyco.com, any @reptilesupplyco.com | 30 Sep 2026 | 5 Oct 2026 | 12 Oct 2026 | Awaiting reply (checked 4 Oct 2026, no reply) |
| 5 | American Safety Distributors (Miami) | AFP full-brim sun shield (B0DKB3TXX5) | Web form (auto-reply expected) | any @americansafetydist.com; 305-262-2234 | 30 Sep 2026 | 5 Oct 2026 | 12 Oct 2026 | Awaiting reply (checked 4 Oct 2026, no reply) |

## Check log

- 1 Oct 2026: Gmail checked for all five supplier domains and draft subjects. No new replies, no auto-replies. CarPro decline already answered 30 Sep. No follow-ups due before 5 Oct. Modern Toyota, Wahl and American Safety have no email thread yet, so follow-up 1 on 5 Oct will need a manual web form or call by Ken unless an address surfaces.
- 2 Oct 2026: Gmail checked for all supplier domains and draft subjects. No replies or auto-replies; only Ken's sent Reptile Supply Co. messages found. No follow-ups due before 5 Oct. Modern Toyota, Wahl and American Safety still have no email thread, so their follow-up 1 remains a manual item for Ken.
- 3 Oct 2026: Gmail checked for all supplier domains and draft subjects. No supplier replies or auto-replies; only Ken's sent Reptile Supply Co. messages and unrelated prep center mail found. No follow-ups due before 5 Oct. Modern Toyota, Wahl and American Safety still have no email thread, so their follow-up 1 on 5 Oct stays a manual item for Ken; Reptile Supply Co. follow-up 1 goes by email on 5 Oct.
- 4 Oct 2026: Gmail checked for all supplier domains and draft subjects. No supplier replies or auto-replies; only Ken's sent Reptile Supply Co. messages and unrelated prep center mail found. No follow-ups due until 5 Oct. Next run sends Reptile Supply Co. follow-up 1 by email; Modern Toyota, Wahl and American Safety follow-up 1 stays a manual item for Ken (no email thread).

## Follow-up rules

1. Follow-up 1 goes out only if no substantive reply has arrived by the due date. Auto-replies do not count as replies.
2. Follow-up 2 goes out one week after follow-up 1 if still silent. After that the SKU is marked "No response" and the shortlist moves to the next candidate in data/wholesale_candidates.json.
3. Follow-ups for the web-form suppliers go by email to the supplier's published address if a reply address has surfaced, otherwise by the same web form.
4. Any reply with pricing, minimums, or account terms is logged to data/metrics.json (wholesale_lane.skus[].status) and summarized to Ken the same day.
5. Nothing gets ordered or paid without Ken's explicit approval.
