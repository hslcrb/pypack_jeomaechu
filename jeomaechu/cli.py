import typer
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import print as rprint
from .core import JeomMaeChu

from typing import Optional

app = typer.Typer(
    help="운명에 맡기는 점심 메뉴 추천기! - 'jeomaechu'만 입력하면 즉시 추천!",
    rich_markup_mode="rich",
    no_args_is_help=False
)
console = Console()
engine = JeomMaeChu()

# Sorthand mapping for categories
CAT_MAP = {
    "한": "Korean (한식)",
    "집": "Real Home (찐 집밥/현실)",
    "일": "Japanese (일본어/일식)",
    "중": "Chinese (중국어/중식)",
    "양": "Western (양식)",
    "아": "Asian (아시아/기타)",
    "상": "Brand (프랜차이즈/매장)"
}

def _perform_pick(category: Optional[str] = None, tag: Optional[str] = None, count: int = 1):
    """Internal helper to avoid Typer OptionInfo issues during direct calls."""
    # Resolve category shorthand
    if category in CAT_MAP:
        category = CAT_MAP[category]
        
    console.print("[bold cyan]점심 메뉴를 추천해드립니다![/bold cyan]\n")
    
    if count > 1:
        results = engine.recommend_many(count, category=category, tag=tag)
        if not results:
            rprint(f"[red]해당 조건에 맞는 메뉴가 없습니다.[/red]")
            return
        
        table = Table(title=f"추천 메뉴 ({len(results)}가지)")
        table.add_column("No.", justify="right", style="dim")
        table.add_column("카테고리", style="yellow")
        table.add_column("메뉴명", style="bold green")
        
        for i, (cat, menu) in enumerate(results, 1):
            table.add_row(str(i), cat or "Tag Pick", menu)
        
        console.print(table)
        return

    result_text = ""
    if category:
        menu = engine.recommend_by_category(category)
        if menu:
            result_text = f"[yellow]{category}[/yellow] 중에서 [bold green]'{menu}'[/bold green] 어떠세요?"
        else:
            rprint(f"[red]존재하지 않는 카테고리입니다: {category}[/red]")
            return
    elif tag:
        menu = engine.recommend_by_tag(tag)
        if menu:
            result_text = f"[yellow]{tag}[/yellow] 느낌으로 [bold green]'{menu}'[/bold green] 어떠세요?"
        else:
            rprint(f"[red]존재하지 않는 태그입니다: {tag}[/red]")
            return
    else:
        cat, menu = engine.recommend_random()
        result_text = f"[yellow]{cat}[/yellow] 카테고리의 [bold green]'{menu}'[/bold green] 어떠세요?"

    console.print(Panel(result_text, title="추천 메뉴", expand=False))

@app.callback(invoke_without_command=True)
def main(
    ctx: typer.Context,
    category: Optional[str] = typer.Option(None, "--category", "-c", help="카테고리 선택"),
    tag: Optional[str] = typer.Option(None, "--tag", "-t", help="태그 선택"),
    count: int = typer.Option(1, "--count", "-n", help="개수 선택")
):
    """점메추(Jeom-Mae-Chu) - 오늘의 점심 메뉴를 정해드립니다."""
    if ctx.invoked_subcommand is None:
        _perform_pick(category, tag, count)

@app.command(name="pick", help="[bold yellow]메뉴 추천 받기 (기본 명령어)[/bold yellow]")
def pick(
    category: Optional[str] = typer.Option(None, "--category", "-c", help="카테고리 선택"),
    tag: Optional[str] = typer.Option(None, "--tag", "-t", help="태그 선택"),
    count: int = typer.Option(1, "--count", "-n", help="개수 선택")
):
    """Pick random lunch menus for today!"""
    _perform_pick(category, tag, count)

# Alias commands
@app.command(name="p", hidden=True)
def pick_alias(
    category: Optional[str] = typer.Option(None, "--category", "-c", help="카테고리 선택"),
    tag: Optional[str] = typer.Option(None, "--tag", "-t", help="태그 선택"),
    count: int = typer.Option(1, "--count", "-n", help="개수 선택")
):
    _perform_pick(category, tag, count)

@app.command(name="cats", help="카테고리 목록 보기")
def list_categories():
    """List all available menu categories."""
    table = Table(title="Menu Categories")
    table.add_column("Category Name", style="cyan")
    for cat in engine.get_categories():
        table.add_row(cat)
    console.print(table)

@app.command(name="c", hidden=True)
def cats_alias():
    list_categories()

@app.command(name="tags", help="태그 목록 보기")
def list_tags():
    """List all available tags/moods."""
    table = Table(title="Menu Tags")
    table.add_column("Tag Name", style="magenta")
    for tag in engine.get_tags():
        table.add_row(tag)
    console.print(table)

@app.command(name="t", hidden=True)
def tags_alias():
    list_tags()

@app.command(name="all", help="[cyan]전체 메뉴 데이터베이스 확인[/cyan]")
def show_all():
    """Show ALL available menus in the database, grouped by category."""
    console.print("[bold green]전체 메뉴 데이터베이스[/bold green]\n")
    
    for category, menus in engine.menus.items():
        table = Table(title=f"[bold yellow]{category}[/bold yellow]", show_header=False, box=None)
        table.add_column("메뉴", style="cyan")
        
        # Display in rows of 6
        cols = 6
        for i in range(0, len(menus), cols):
            row_items = menus[i:i + cols]
            table.add_row(", ".join(row_items))
        
        console.print(table)
        console.print("-" * 40)

@app.command(name="a", hidden=True)
def all_alias():
    show_all()

if __name__ == "__main__":
    app()
