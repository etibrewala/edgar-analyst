import httpx
import typer

app = typer.Typer()


@app.command()
def ping(ticker: str = "AAPL") -> None:
    """Look up a ticker's CIK to confirm EDGAR access."""
    from edgar_analyst.config import settings

    r = httpx.get(
        "https://www.sec.gov/files/company_tickers.json",
        headers={"User-Agent": settings.sec_user_agent},
    )
    r.raise_for_status()
    match = next(v for v in r.json().values() if v["ticker"] == ticker.upper())
    typer.echo(f"{ticker.upper()} -> CIK {match['cik_str']:010d} ({match['title']})")


@app.command()
def version() -> None:
    """Print the version."""
    typer.echo("edgar-analyst 0.1.0")
