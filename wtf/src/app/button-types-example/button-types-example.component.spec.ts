import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ButtonTypesExampleComponent } from './button-types-example.component';

describe('ButtonTypesExampleComponent', () => {
  let component: ButtonTypesExampleComponent;
  let fixture: ComponentFixture<ButtonTypesExampleComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ButtonTypesExampleComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ButtonTypesExampleComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
