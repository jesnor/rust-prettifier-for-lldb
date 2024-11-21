from test_harness import expect_command_output, expect_summaries


def test_u8(tmpdir):
    src = """
        let x: u8 = 65;
    """
    expect_summaries(tmpdir, src, {
        "x": "65",
    })


def test_char(tmpdir):
    src = """
        let x: char = 'A';
        let y: char = '\\n';
    """
    expect_summaries(tmpdir, src, {
        "x": "'A'",
        "y": "U+0x0000000A"
    })


def test_str(tmpdir):
    src = """
        let x: &str = "foo";
        let y: String = "bar".into();
    """
    expect_summaries(tmpdir, src, {
        "x": "\"foo\"",
        "y": "\"bar\""
    })


def test_rc(tmpdir):
    src = """
        use std::rc::Rc;
        let x = Rc::new(42);
    """
    expect_summaries(tmpdir, src, {
        "x": "(refs:1) 42",
    })


def test_box(tmpdir):
    src = """
        let x = Box::new(42);
    """
    # TODO: currently raw summary text is just the pointer hex value,
    # consider showing Box(T) ?
    expect_command_output(tmpdir, src, [
        ("v *x", "(int) *x = 42\n"),
    ])
