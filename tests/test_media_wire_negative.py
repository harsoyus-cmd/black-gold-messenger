from core.media.wire import decode_wire_payload


INVALID_PAYLOADS = (
    "",
    "{}",
    '{"media_type":"IMAGE"}',
    '{"media_type":"INVALID","name":"x.jpg","size":1,"protocol_version":"0.1"}',
)


for payload in INVALID_PAYLOADS:
    try:
        decode_wire_payload(payload)
    except (TypeError, ValueError):
        continue

    raise AssertionError(
        f"Invalid payload was accepted: {payload!r}"
    )


print("BGM Media Wire Negative Test: PASS")
print("Rejected:", len(INVALID_PAYLOADS))
