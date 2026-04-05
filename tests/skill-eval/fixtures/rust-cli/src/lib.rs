pub fn parse_port(raw: &str) -> Result<u16, String> {
    let port = raw.trim().parse::<u16>().map_err(|_| "invalid port".to_string())?;
    Ok(port)
}

#[cfg(test)]
mod tests {
    use super::parse_port;

    #[test]
    fn rejects_blank_input() {
        assert!(parse_port("   ").is_err());
    }

    #[test]
    fn rejects_zero_port() {
        assert!(parse_port("0").is_err());
    }
}
